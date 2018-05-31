import tkinter
import tkinter.messagebox
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
        menubar.add_cascade(label='new game', command=self.onResetClick)
        self.master['menu'] = menubar

        # Add buttons to window.
        self.button_list = [[tkinter.Button(self.master) for x in range(GAME_SETTING['x'])] for y in range(GAME_SETTING['y'])]
        for y,button_row in enumerate(self.button_list):
            for x,button in enumerate(button_row):
                button['text'] = '(' + str(x) + ',' + str(y) + ')'
                button.grid(column=x, row=y)
                button['height'] = 1
                button['width'] = 2
               #button.bind('<Button-1>', lambda event, axis={'x':x,'y':y}:self.onLeftClick(axis))
                button['command'] = lambda axis={'x':x,'y':y}:self.onLeftClick(axis)
                button.bind('<Button-3>', lambda event, axis={'x':x,'y':y}:self.onRightClick(axis))

        # Create a game instance and reset it.
        self.game = Minesweeper()
        self.game.newGame(size_x=GAME_SETTING['x'], size_y=GAME_SETTING['y'], mine_number=GAME_SETTING['mines'])
        self.nextState()

    def onResetClick(self):
        '''
        onResetClick()
            Callback function for click reset menu.
        '''
        print("Reset click!")
        
        self.game.newGame(size_x=GAME_SETTING['x'], size_y=GAME_SETTING['y'], mine_number=GAME_SETTING['mines'])
        self.nextState()

    def onLeftClick(self, axis):
        '''
        onLeftClick(axis)
            Callback function for left click button.
            axis: The axis for target button.
        '''
       #print("Button(", axis['x'], ',', axis['y'], ') be left clicked!', sep='')
        
        self.game.open(x=axis['x'], y=axis['y'])
        self.nextState()

    def onRightClick(self, axis):
        '''
        onRightClick(axis)
            Callback function for right click button.
            axis: The axis for target button.
        '''
       #print("Button(", axis['x'], ',', axis['y'], ') be right clicked!', sep='')

        self.game.flag(x=axis['x'], y=axis['y'])
        self.nextState()

    def nextState(self):
        '''
        nextState()
            None.
        '''
        unknown_count = 0
        boom_count = 0
        game_map = self.game.getMap()
        for y,game_map_row in enumerate(game_map):
            for x,game_map_node in enumerate(game_map_row):
                self.button_list[y][x]['text'] = SYMBOL_LIST[game_map[y][x]]

                if game_map_node == 'unknown':
                    self.button_list[y][x]['relief'] = tkinter.RAISED
                    unknown_count = unknown_count + 1
                elif game_map_node == 'flag':
                    self.button_list[y][x]['relief'] = tkinter.RAISED
                elif game_map_node == 9:
                    tkinter.messagebox.showinfo('Boom', '_:(´°ω°`」 ∠):_')
                    boom_count = boom_count + 1
                else:
                    self.button_list[y][x]['relief'] = tkinter.SUNKEN

        if unknown_count==0 and boom_count==0:
            print('uc:',unknown_count)
            tkinter.messagebox.showinfo('Win', 'Y(9q9)Y')
                
                
       #self.button_list[axis['x']][axis['y']]['text'] = SYMBOL_LIST['mine']
       #self.button_list[axis['x']][axis['y']]['text'] = SYMBOL_LIST['flag']
       #object['state'] = tkinter.DISABLED   # Disable button...
       #object['state'] = tkinter.NORMAL     # Enable button...

       #object['relief'] = tkinter.SUNKEN    # Seem pushed...
       #object['relief'] = tkinter.RAISED    # Seem released...

if __name__ == '__main__':

    gui = GUI(master=tkinter.Tk())
    gui.mainloop()
