import tkinter
from Minesweeper import Minesweeper

# Game settings.
GAME_SETTING = {'x':10, 'y':10, 'mines': 10}

# Button symbles.
SYMBOL_LIST = {'flag':'⚑','unknown':'', \
               0:'', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'✹'}

class   GUI(tkinter.Frame):
    '''
    Class GUI
        The GUI for minesweeper game.
    '''

    def __init__(self, master=None):
        '''
        Constructor(master)
            master: Toplevel widget.
        '''
        # Parent constructor.
        super().__init__(master)

        # Main window setting.
        self.master.resizable(False, False)     # Fixed window size.
        self.master.title('Minesweeper')        # Set window title.

        # Add menu to window.
        menubar = tkinter.Menu(self.master)
        menubar.add_cascade(label='Reset', command=self.onResetClick)
        self.master['menu'] = menubar

        # Add buttons to window.
        self.button_list = list()
        for y in range(GAME_SETTING['y']):
            button_row = list()
            for x in range(GAME_SETTING['x']):
                button = tkinter.Button(self.master)
                button['text'] = ''
                button.grid(column=x, row=y)
                button['height'] = 1
                button['width'] = 2
                button.bind('<Button-1>', lambda event, axis={'x':x,'y':y}:self.onLeftClick(axis))
                button.bind('<Button-3>', lambda event, axis={'x':x,'y':y}:self.onRightClick(axis))
                button_row.append(button)
            self.button_list.append(button_row)

        # Create a game instance and reset it.
        self.game = Minesweeper()
        self.game.newGame(GAME_SETTING['x'], GAME_SETTING['y'], GAME_SETTING['mines'])
        self.nextState()

    def onResetClick(self):
        '''
        onResetClick()
            Callback function for click reset menu.
        '''
        print("Reset click!")
        
        self.game.reset()
        self.nextState()

    def onLeftClick(self, axis):
        '''
        onLeftClick(axis)
            Callback function for left click button.
            axis: The axis for target button.
        '''
       #print("Button(", axis['x'], ',', axis['y'], ') be left clicked!', sep='')
        
        self.game.open(axis['y'],axis['x'])
        self.nextState()

    def onRightClick(self, axis):
        '''
        onRightClick(axis)
            Callback function for right click button.
            axis: The axis for target button.
        '''
       #print("Button(", axis['x'], ',', axis['y'], ') be right clicked!', sep='')

        self.game.setFlag(axis['x'], axis['y'])
        self.nextState()

    def nextState(self):
        '''
        nextState()
            None.
        '''
        game_map = self.game.getMap()
        for y in range(GAME_SETTING['y']):
            for x in range(GAME_SETTING['x']):
                if game_map[y][x] == 'unknown':
                    self.button_list[y][x]['relief'] = tkinter.RAISED
                else:
                    self.button_list[y][x]['relief'] = tkinter.SUNKEN

                self.button_list[x][y]['text'] = SYMBOL_LIST[game_map[y][x]]
                
       #self.button_list[axis['x']][axis['y']]['text'] = SYMBOL_LIST['mine']
       #self.button_list[axis['x']][axis['y']]['text'] = SYMBOL_LIST['flag']
       #object['state'] = tkinter.DISABLED   # Disable button...
       #object['state'] = tkinter.NORMAL     # Enable button...

       #object['relief'] = tkinter.SUNKEN    # Seem pushed...
       #object['relief'] = tkinter.RAISED    # Seem released...

if __name__ == '__main__':

    gui = GUI(master=tkinter.Tk())
    gui.mainloop()
