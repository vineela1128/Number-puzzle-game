import tkinter as tk
from tkinter import messagebox
import random

SIZE = 3

class PuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Puzzle Game")
        self.root.geometry("450x600")
        self.root.config(bg="#1e293b")

        self.moves = 0
        self.seconds = 0
        self.running = True

        title = tk.Label(
            root,
            text="🧩 Number Puzzle",
            font=("Arial", 22, "bold"),
            bg="#1e293b",
            fg="white"
        )
        title.pack(pady=10)

        self.info = tk.Label(
            root,
            text="Moves: 0   Time: 0s",
            font=("Arial", 14),
            bg="#1e293b",
            fg="white"
        )
        self.info.pack()

        self.frame = tk.Frame(root, bg="#1e293b")
        self.frame.pack(pady=20)

        self.tiles = list(range(1, 9)) + [0]
        self.shuffle_tiles()

        self.buttons = []

        for i in range(SIZE):
            row = []
            for j in range(SIZE):
                btn = tk.Button(
                    self.frame,
                    width=6,
                    height=3,
                    font=("Arial", 20, "bold"),
                    bg="#38bdf8",
                    fg="white",
                    command=lambda r=i, c=j: self.move_tile(r, c)
                )
                btn.grid(row=i, column=j, padx=3, pady=3)
                row.append(btn)
            self.buttons.append(row)

        control = tk.Frame(root, bg="#1e293b")
        control.pack()

        tk.Button(
            control,
            text="🔀 Shuffle",
            font=("Arial", 12, "bold"),
            bg="#22c55e",
            fg="white",
            command=self.shuffle_game
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            control,
            text="🔄 Restart",
            font=("Arial", 12, "bold"),
            bg="#f97316",
            fg="white",
            command=self.restart_game
        ).grid(row=0, column=1, padx=10)

        self.update_board()
        self.update_timer()

    def shuffle_tiles(self):
        random.shuffle(self.tiles)

    def update_board(self):
        for i in range(SIZE):
            for j in range(SIZE):
                value = self.tiles[i * SIZE + j]

                if value == 0:
                    self.buttons[i][j].config(
                        text="",
                        bg="#0f172a"
                    )
                else:
                    self.buttons[i][j].config(
                        text=str(value),
                        bg="#38bdf8"
                    )

        self.info.config(
            text=f"Moves: {self.moves}   Time: {self.seconds}s"
        )

    def move_tile(self, row, col):
        index = row * SIZE + col
        empty = self.tiles.index(0)

        erow = empty // SIZE
        ecol = empty % SIZE

        if abs(row - erow) + abs(col - ecol) == 1:
            self.tiles[index], self.tiles[empty] = (
                self.tiles[empty],
                self.tiles[index]
            )

            self.moves += 1
            self.update_board()

            if self.check_win():
                self.running = False
                messagebox.showinfo(
                    "Winner",
                    f"🎉 You solved it!\nMoves: {self.moves}\nTime: {self.seconds}s"
                )

    def check_win(self):
        return self.tiles == [1,2,3,4,5,6,7,8,0]

    def update_timer(self):
        if self.running:
            self.seconds += 1
            self.update_board()

        self.root.after(1000, self.update_timer)

    def shuffle_game(self):
        random.shuffle(self.tiles)
        self.moves = 0
        self.seconds = 0
        self.running = True
        self.update_board()

    def restart_game(self):
        self.tiles = list(range(1, 9)) + [0]
        random.shuffle(self.tiles)
        self.moves = 0
        self.seconds = 0
        self.running = True
        self.update_board()

root = tk.Tk()
game = PuzzleGame(root)
root.mainloop()