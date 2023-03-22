import random

class Drawer:

    @staticmethod
    def draw_frame(map, characters):
        for y, row in enumerate(map):
            for x, pixel in enumerate(row):
                char = "#" if pixel == 1 else "."
                for character in characters:
                    if character.x == x and character.y == y and character.visible:
                        char = character.icon
                print(char, end="")
            print()

class Character:
    def __init__(self, x, y, icon):
        self.x = x
        self.y = y
        self.icon = icon
        self.visible = True
    def move(self):
        pass

class Player(Character):
    def move(self):
        moves = {"a": (-1, 0), "d": (1, 0), "w": (0, -1), "s": (0, 1)}
        key = input("Куда идти?").lower()
        while key not in ("a", "s", "w", "d"):
            key = input("Куда идти?").lower()
        x, y = moves[key]
        self.x += x
        self.y += y

class Enemy(Character):
    def move(self):
        moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        x, y = random.choice(moves)
        self.x += x
        self.y += y

class Game:
    map = [[0 if 0 < col < 9 else 1 for col in range(10)] if 0 < row < 9 else [1]*10 for row in range(10)]

    def get_player(self):
        player = [character for character in self.characters if isinstance(character, Player)]
        if player:
            return player[0]
        else:
            return None
        
    characters: list[Character] = []
    def update(self):
        player = self.get_player()
        if player:
            for character in self.characters:
                if abs(character.x - player.x) <= 2 and abs(character.y - player.y) <= 2:
                    character.visible = True
                else:
                    character.visible = False

        Drawer.draw_frame(self.map, self.characters)

    def fixed_update(self):
        for character in self.characters:
            character.move()

        self.update()

game = Game()
game.characters.append(Player(5, 5, "@"))
game.characters.append(Enemy(5, 2, "x"))
game.characters.append(Enemy(2, 2, "o"))
game.update()
for i in range(10):
    game.fixed_update()