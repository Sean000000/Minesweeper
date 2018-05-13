import random

class Minesweeper:
    def reset(self):
        # Create game map.
        self.map = [[0 for x in range(self.x)] for y in range(self.y)]

       #self.map[y][x] = '*'
        # Set mines.
        mine_list = random.sample(range(self.x*self.y), self.mine_count)
        for mine in mine_list:
            self.map[mine//self.x][mine%self.x] = 9

        # Set mine hint.
        for y in range(self.y):
            for x in range(self.x):
                if self.map[y][x] == 9:
                    continue
                else:
                    # Left-Top
                    if x>0 and y>0 and self.map[y-1][x-1]==9:
                        self.map[y][x] += 1
                    # Top
                    if y>0 and self.map[y-1][x]==9:
                        self.map[y][x] += 1
                    # Right-Top
                    if x<(self.x-1) and y>0 and self.map[y-1][x+1]==9:
                        self.map[y][x] += 1
                    # Left
                    if x>0 and self.map[y][x-1]==9:
                        self.map[y][x] += 1
                    # Right
                    if x<(self.x-1) and self.map[y][x+1]==9:
                        self.map[y][x] += 1
                    # Left-Down
                    if x>0 and y<(self.y-1) and self.map[y+1][x-1]==9:
                        self.map[y][x] += 1
                    # Down
                    if y<(self.y-1) and self.map[y+1][x]==9:
                        self.map[y][x] += 1
                    # Right-Down
                    if x<(self.x-1) and y<(self.y-1) and self.map[y+1][x+1]==9:
                        self.map[y][x] += 1

    def sweep(self, x, y):
        pass
    def __init__(self, x, y, mine_count):
        # Get game setting.
        self.x = x
        self.y = y
        self.mine_count = mine_count
        # Reset game.
        self.reset()

    def printMap(self):
        for y in self.map:
            for data in y:
                print(data, ' ', end='')
            print()

if __name__ == '__main__':
    new = Minesweeper(10, 10, 99)
    new.printMap()
