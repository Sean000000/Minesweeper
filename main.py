import random
import tkinter as tk

class Minesweeper:
    '''
    Class: Minesweeper
    '''

    def reset(self):
        '''
        Method: reset()

        '''
        # Create game map. (self.map[y][x] = {value,visible})
        self.map = [[{'value':0,'visible':False} for x in range(self.x)] for y in range(self.y)]

        # Set random mines map.
        mine_list = random.sample(range(self.x*self.y), self.mine_count)
        mine_list = [0,11,22,33,44,55,66,77,88,99]
        for mine in mine_list:
            self.map[mine//self.x][mine%self.x]['value'] = 9

        # Set mine hint.
        for y in range(self.y):
            for x in range(self.x):
                if self.map[y][x]['value'] == 9:
                    #
                    continue
                else:
                    #
                    mines = 0

                    # Check Left-Top
                    if x>0 and y>0 and self.map[y-1][x-1]['value']==9:
                        mines += 1
                    # Check Top
                    if y>0 and self.map[y-1][x]['value']==9:
                        mines += 1
                    # Check Right-Top
                    if x<(self.x-1) and y>0 and self.map[y-1][x+1]['value']==9:
                        mines += 1
                    # Check Left
                    if x>0 and self.map[y][x-1]['value']==9:
                        mines += 1
                    # Check Right
                    if x<(self.x-1) and self.map[y][x+1]['value']==9:
                        mines += 1
                    # Check Left-Down
                    if x>0 and y<(self.y-1) and self.map[y+1][x-1]['value']==9:
                        mines += 1
                    # Check Down
                    if y<(self.y-1) and self.map[y+1][x]['value']==9:
                        mines += 1
                    # Check Right-Down
                    if x<(self.x-1) and y<(self.y-1) and self.map[y+1][x+1]['value']==9:
                        mines += 1

                    #
                    self.map[y][x]['value'] = mines
        #
        self.game_over = False

    def sweep(self, x, y):
        '''
        Method: sweep(x, y)
        '''
        #
        if self.map[y][x]['visible'] == True:
            return
        self.map[y][x]['visible'] = True

        #
        if self.map[y][x]['value'] == 9:
            self.game_over = True
            return

        if self.map[y][x]['value'] == 0:
            # Check Left-Top
            if x>0 and y>0:
                self.sweep(x-1, y-1)
            # Check Top
            if y>0:
                self.sweep(x, y-1)
            # Check Right-Top
            if x<(self.x-1) and y>0:
                self.sweep(x+1, y-1)
            # Check Left
            if x>0:
                self.sweep(x-1, y)
            # Check Right
            if x<(self.x-1):
                self.sweep(x+1, y)
            # Check Left-Down
            if x>0 and y<(self.y-1):
                self.sweep(x-1, y+1)
            # Check Down
            if y<(self.y-1):
                self.sweep(x, y+1)
            # Check Right-Down
            if x<(self.x-1) and y<(self.y-1):
                self.sweep(x+1, y+1)
        
    def __init__(self, x, y, mine_count):
        '''
        Method: __init__(x, y, mine_count)
        '''
        # Get game setting.
        self.x = x
        self.y = y
        self.mine_count = mine_count
        # Reset game.
        self.reset()

    def printValue(self):
        '''
        Method: printValue()
        '''
        for list_on_map in self.map:
            for dict_on_list in list_on_map:
                print(dict_on_list['value'], ' ', end='')
            print()

    def printVisible(self):
        '''
        Method: printVisible()
        '''
        for list_on_map in self.map:
            for dict_on_list in list_on_map:
                print(dict_on_list['visible'], ' ', end='')
            print()

    def getMap(self):
        '''
        Method: getMap()
        '''
        new_map = list()
        for list_on_map in self.map:
            new_list = list()
            for dict_on_list in list_on_map:
                if dict_on_list['visible'] == False:
                    new_list.append(None)
                else:
                    new_list.append(dict_on_list['value'])
            new_map.append(new_list)
        return new_map

class   UI(tk.Frame):
    '''
    Class: UI
    '''
    def __init__(self, master=None):
        '''
        Method: __init__(master)
        '''
        super().__init__(master)
        self.grid()
        self.create_widgets()

        
        new = Minesweeper(10, 10, 10)
       #new.printValue()
       #new.printVisible()
        print(new.getMap())
        new.sweep(9,0)
       #new.printValue()
       #new.printVisible()
        print(new.getMap())


    def create_widgets(self):
        '''
        Method: create_widgets()
        '''
        for y in range(10):
            for x in range(10):
                self.new = tk.Button(self)
                self.new["text"] = "☠"
                self.new["command"] = self.say_hi
                self.new.grid(row=x, column=y)

    def say_hi(self):
        '''
        Method: create_widgets()
        '''
        print("hi there, everyone!")


if __name__ == '__main__':
    root = tk.Tk()
    ui = UI(master=root)
    ui.mainloop()
