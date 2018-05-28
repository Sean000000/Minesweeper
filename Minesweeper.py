import random

class Minesweeper:
    '''
    Class Minesweeper
        Description:
        The class for minesweeper game.
    '''
    def __init__(self):
        '''
        Constructor()
        Description:
            Constructor for class Minesweeper.
        Parameters:
            None.
        '''
        self.newGame(10, 10, 10)

    class Node:
        '''
        Class Node
        Description:
            Inner class for map node.
        '''
        def __init__(self, visible, value, flag):
            '''
            Constructor(visible, value, flag)
            Description:
                Constructor for class Node.
            Parameters:
                visible -
                value -
                flag -
            '''
            self.visible = visible
            self.value = value
            self.flag = flag
        def setVisible(self, state):
            '''
            setVisible(state)
            Description:
                Setter for visible.
            Parameters:
                state -
            '''
            self.visible = state
        def getVisible(self):
            '''
            getVisible()
            Description:
                Getter for visible.
            Parameters:
                None.
            '''
            return self.visible
        def setValue(self, value):
            '''
            setValue(state)
            Description:
                Setter for value.
            Parameters:
                value -
            '''
            self.value = value
        def getValue(self):
            '''
            getValue()
            Description:
                Getter for value.
            Parameters:
                None.
            '''
            return self.value
        def setFlag(self, state):
            '''
            setFlag(state)
            Description:
                Setter for flag.
            Parameters:
                state -
            '''
            self.flag = state
        def getFlag(self):
            '''
            getFlag()
            Description:
                Getter for flag.
            Parameters:
                None.
            '''
            return self.flag

    def newGame(self, size_x, size_y, mine_number):
        '''
        newGame(size_x, size_y, mine_number)
        Description:
            Start a new game.
        Parameters:
            size_x -
            size_y -
            mine_number -
        '''
        # Get game setting.
        self.size_x = size_x
        self.size_y = size_y
        self.mine_number = mine_number

        # Create game map.
        self.map = [[self.Node(visible=False,value=0,flag=False) for x in range(self.size_x)] for y in range(self.size_y)]

        # Put mines to random axis on the map.
        random_list = random.sample(range(self.size_x*self.size_y), self.mine_number)
        random_list = [0,9,11,18,22,27,33,36,44,45]  # Just for test...

        for random_number in random_list:
            x = random_number %  self.size_x
            y = random_number // self.size_x
            self.map[y][x].setValue(9)    # The number 9 means mine.

        # Mark mines count on the map.
        for y in range(self.size_y):
            for x in range(self.size_x):
                if self.map[y][x].getValue() == 9:
                    continue
                else:
                    # To count around mines.
                    # Warning: This part used short-circuit evaluation, so the getValue()
                    #          should be execute on the last.
                    around_mines = 0
                    if y>0 and x>0 and self.map[y-1][x-1].getValue()==9:                                # Left-Top...
                        around_mines += 1
                    if y>0 and self.map[y-1][x].getValue()==9:                                          # Top...
                        around_mines += 1
                    if y>0 and x<(self.size_x-1) and self.map[y-1][x+1].getValue()==9:                  # Right-Top...
                        around_mines += 1
                    if x>0 and self.map[y][x-1].getValue()==9:                                          # Left...
                        around_mines += 1
                    if x<(self.size_x-1) and self.map[y][x+1].getValue()==9:                            # Right...
                        around_mines += 1
                    if y<(self.size_y-1) and x>0 and self.map[y+1][x-1].getValue()==9:                  # Left-Down...
                        around_mines += 1
                    if y<(self.size_y-1) and self.map[y+1][x].getValue()==9:                            # Down...
                        around_mines += 1
                    if y<(self.size_y-1) and x<(self.size_x-1) and self.map[y+1][x+1].getValue()==9:    # Right-Down...
                        around_mines += 1
                    self.map[y][x].setValue(around_mines)                                               # Write-back to the node.

    def open(self, x, y):
        '''
        open(x, y)
        Description:
            Open a node on the map.
        Parameters:
            x -
            y -
        '''
        # Let the node to visible.
        if self.map[y][x].getVisible() == True:
            return
        self.map[y][x].setVisible(True)

        # Open around node when value is 0.
        if self.map[y][x].getValue() == 0:
            if y > 0:                   # Top...
                self.open(x, y-1)
            if x > 0:                   # Left...
                self.open(x-1, y)
            if x < (self.size_x-1):     # Right...
                self.open(x+1, y)
            if y < (self.size_y-1):     # Down...
                self.open(x, y+1)

    def flag(self, x, y, state):
        '''
        flag(x, y, state)
        Description:
            Set node as flag.
        Parameters:
            x -
            y -
            state -
        '''
        self.map[y][x].setFlag(state)

    def getMap(self):
        '''
        getMap()
        Description:
            Get last game map.
        Parameters:
            None.
        '''
        game_map = list()
        for y in range(self.size_y):
            map_row = list()
            for x in range(self.size_x):
                if self.map[y][x].getVisible() == False:
                    map_row.append('unknown')
                elif self.map[y][x].getFlag() == True:
                    map_row.append('flag')
                else:
                    map_row.append(self.map[y][x].getValue())
            game_map.append(map_row)
        return game_map
