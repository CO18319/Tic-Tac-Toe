import tkinter as tk
import tic_tac_toe as t


class guiBoard(t.solve):

    def __init__(self):
        # initialize tic-tac-toe board
        super().__init__()

        # initialize graphical window
        self.root = tk.Tk()

        # set window's width and height
        width = 357
        height = 400

        # get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # calculate position of x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.title("TIC-TAC-TOE")

        self.root['background'] = "white smoke"

        # tuple of lists representing graphical tic-tac-toe cells
        self.gui_board = ([], [], [])

        # set start button
        self.start = tk.Button(self.root, padx=10, pady=10, relief="flat", bg="light yellow", fg="brown4", text="START",
                               font=('arial', 20, 'bold'),
                               bd=1)
        self.start.config(command=lambda: self.start_game())
        self.start.grid(row=0, column=1)

        # set reset button
        self.reset = tk.Button(self.root, padx=10, pady=10, relief="flat", bg="brown4", fg="white", state="disabled",
                               text="RESET",
                               font=('arial', 20, 'bold'),
                               bd=1)
        self.reset.config(command=lambda: self.reset_game())
        self.reset.grid(row=0, column=3)

        # set label for displaying result
        self.label = tk.Label(self.root, bg="brown4", fg="white", font=('arial', 25, 'bold'))

        # show cells of board as buttons on the window
        for i in range(t.size):
            for j in range(t.size):
                self.gui_board[i].append(
                    tk.Button(self.root, padx=1, bg="white", width=3, text="", state="disabled",
                              font=('arial', 50, 'bold'),
                              bd=1))
                self.gui_board[i][j].config(command=lambda row=i, col=j: self.button_click(row, col))
                self.gui_board[i][j].grid(row=i + 1, column=j + 1)

    # function called when start button is clicked
    def start_game(self):
        for i in range(t.size):
            for j in range(t.size):
                self.gui_board[i][j]['state'] = "normal"
        # enable reset button
        self.reset['state'] = "normal"
        # disable start button
        self.start['state'] = "disabled"

    # function called when reset game button is clicked
    def reset_game(self):
        for i in range(t.size):
            for j in range(t.size):
                self.gui_board[i][j]['text'] = ""
                self.gui_board[i][j]['state'] = "normal"
        super().__init__()
        self.label.grid_forget()

    # function called when human plays the turn
    def button_click(self, row, col):
        if self.board[row][col] == "_":
            # check for win or a tie
            self.display_result()
            self.board[row][col] = t.human
            self.gui_board[row][col].config(text=t.human, fg=t.colour[t.human])
            # check for a win or a tie
            self.display_result()
            current_player = t.ai
            [row_1, col_1] = self.best_move()
            if self.gui_board[row_1][col_1]['text'] != t.human:
                self.gui_board[row_1][col_1].after(100, lambda: self.gui_board[row_1][col_1].config(text=t.ai,
                                                                                                    fg=t.colour[t.ai]))
                # check for a win or a tie
                self.display_result()
                current_player = t.human

    def display_result(self):
        # check if a player won or there is a tie
        result = t.check_winner(self.board)
        # output result if a player is won
        if result == t.ai or result == t.human:
            self.label.config(text=result + " Won !!")
            self.label.grid(row=5, column=0, columnspan=5)
            for i in range(t.size):
                for j in range(t.size):
                    self.gui_board[i][j]['state'] = "disabled"

        # output result if there is a tie
        elif result == 'tie':
            self.label.config(text="It's a tie !!")
            self.label.grid(row=5, column=0, columnspan=5)
            for i in range(t.size):
                for j in range(t.size):
                    self.gui_board[i][j]['state'] = "disabled"


if __name__ == '__main__':
    tic_tac_toe = guiBoard()
    tic_tac_toe.root.mainloop()
