import tkinter as tk

GAME_SETTING = {'x':10, 'y':10, 'mines': 10}

class   GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.grid()
        self.master.title('Minesweeper')

        menubar = tk.Menu(master)
        menubar.add_cascade(label='Reset', command=self.onResetClick)
        self.master.config(menu=menubar)

        for x in range(GAME_SETTING['x']):
            for y in range(GAME_SETTING['y']):
                self.button = tk.Button(master)
                self.button['text'] = '(' + str(x) + ',' + str(y) +')'
                self.button.grid(column=x, row=y)
                self.button.bind('<Button-1>', lambda event, object=self.button:self.onLeftClick(object))
                self.button.bind('<Button-3>', lambda event, object=self.button:self.onRightClick(object))

    def onResetClick(self):
        print("Reset click!")

    def onLeftClick(self, object):
        print("Left click!")

    def onRightClick(self, object):
        print("Right click!")

       #object['state'] = tk.DISABLED   # Disable button...
       #object['state'] = tk.NORMAL     # Enable button...

       #object['relief'] = tk.SUNKEN    # Seem pushed...
       #object['relief'] = tk.RAISED    # Seem released...

if __name__ == '__main__':
    root = tk.Tk()
    app = GUI(master=root)
    app.mainloop()
