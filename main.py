from tkinter import Tk, Entry, StringVar, Button


class SolveSudoku:

    def add_zeros(self):
        for i in range(9):
            for j in range(9):
                if list_values[i][j].get() not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    list_values[i][j].set(0)

    def find_empty(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if list_values[i][j].get() == '0':
                    return i, j
        return None

    def valid(self, nr, row, col):
        for j in range(0, 9):
            if list_values[row][j].get() == str(nr):
                return False

        for i in range(0, 9):
            if list_values[i][col].get() == str(nr):
                return False

        row_initial_pos = 3 * (row // 3)
        col_initial_pos = 3 * (col // 3)
        row_finish_pos = row_initial_pos + 3
        col_finish_pos = col_initial_pos + 3

        for row in range(row_initial_pos, row_finish_pos):
            for col in range(col_initial_pos, col_finish_pos):
                if list_values[row][col].get() == str(nr):
                    return False

        return True

    def solve(self):
        if self.find_empty() is None:
            return True
        else:
            row = self.find_empty()[0]
            col = self.find_empty()[1]

        for i in range(1, 10):
            if self.valid(i, row, col):
                list_values[row][col].set(str(i))

                if self.solve():
                    return True

                list_values[row][col].set(0)


class Interface:
    def __init__(self, window):

        self.window = window
        window.title("Sudoku Solver")

        self.table = []
        for i in range(1, 10):
            self.table += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]

        for i in range(0, 9):
            for j in range(0, 9):
                if (i < 3 or i > 5) and 2 < j < 6:
                    color = "#c6b7fe"

                elif 2 < i < 6 and (j < 3 or j > 5):
                    color = "#c6b7fe"

                else:
                    color = "#fff9ea"

                self.table[i][j] = Entry(window, bg=color, width=2, justify='center', font=('arial', 32, 'bold'),
                                         textvar=list_values[i][j],
                                         highlightthickness=1, highlightbackground="black")

                self.table[i][j].bind('<Motion>', lambda x: self.correct_grid())

                self.table[i][j].grid(row=i, column=j)

        solve_button = Button(window, text="SOLVE", command=self.solve_sudoku)
        solve_button.grid(column=1, row=20)
        reset_button = Button(window, text="RESET", command=self.reset)
        reset_button.grid(column=7, row=20)

    def reset(self):
        for i in range(0, 9):
            for j in range(0, 9):
                list_values[i][j].set('')

    def solve_sudoku(self):
        sudoku = SolveSudoku()
        sudoku.add_zeros()
        sudoku.solve()

    @staticmethod
    def correct_grid():
        for i in range(9):
            for j in range(9):
                if list_values[i][j].get() == '':
                    continue
                if len(list_values[i][j].get()) > 1 or list_values[i][j].get() not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    list_values[i][j].set('')


root = Tk()
root.title("Sudoku Solver")
root.geometry('486x540')
root.resizable(False, False)

list_values = []
for i in range(9):
    list_values += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]

for row in range(9):
    for col in range(9):
        list_values[row][col] = StringVar(root)

window = Interface(root)
root.mainloop()
