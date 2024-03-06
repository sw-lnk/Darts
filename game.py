import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk

import locale


class Player:
    def __init__(self, player_name: str, start_score: int = 501):
        self.name: str = player_name
        self.score: int = start_score
        self.scorings: list[tuple[int, int]] = []
        self.legs_won: int = 0


class Game(ctk.CTkFrame):
    def __init__(
        self,
        master,
        player_name_1: str,
        player_name_2: str,
        start_score: int = 501,
        legs_to_win: int = 3,
        double_out: bool = False,
        double_in: bool = False,
        board_no: int = 1,
    ):
        super().__init__(master)

        # Player
        self.p1: Player = Player(player_name_1, start_score)
        self.p2: Player = Player(player_name_2, start_score)

        # GUI values
        self.score_p1: tk.IntVar = tk.IntVar(self, self.p1.score)
        self.legs_p1: tk.IntVar = tk.IntVar(self, self.p1.legs_won)
        self.score_p2: tk.IntVar = tk.IntVar(self, self.p2.score)
        self.legs_p2: tk.IntVar = tk.IntVar(self, self.p2.legs_won)

        # GUI
        self.name_size: int = 35
        self.score_size: int = 50

        ## Label to show player name and score
        self.label_name_p1 = ctk.CTkLabel(
            self,
            text=self.p1.name,
            font=ctk.CTkFont(size=self.name_size),
        )

        self.label_score_p1 = ctk.CTkLabel(
            self,
            textvariable=self.score_p1,
            font=ctk.CTkFont(size=self.score_size),
        )

        self.label_name_p2 = ctk.CTkLabel(
            self,
            text=self.p2.name,
            font=ctk.CTkFont(size=self.name_size),
        )

        self.label_score_p2 = ctk.CTkLabel(
            self,
            textvariable=self.score_p2,
            font=ctk.CTkFont(size=self.score_size),
        )

        ## Label to show board number
        self.label_name_board = ctk.CTkLabel(
            self,
            text=f"Board {board_no}",
            font=ctk.CTkFont(size=int(self.name_size * 0.6)),
        )

        ## Show game overview
        self.game_overview = ctk.CTkFrame(self)
        self.label_legs_p1 = ctk.CTkLabel(
            self.game_overview,
            textvariable=self.legs_p1,
            font=ctk.CTkFont(size=int(self.score_size * 0.4)),
        )
        self.label_legs_p2 = ctk.CTkLabel(
            self.game_overview,
            textvariable=self.legs_p2,
            font=ctk.CTkFont(size=int(self.score_size * 0.4)),
        )
        self.label_legs_p1.grid(row=1, column=1)
        ctk.CTkLabel(
            self.game_overview,
            text="-",
            font=ctk.CTkFont(size=int(self.score_size * 0.4)),
        ).grid(row=1, column=2)
        self.label_legs_p2.grid(row=1, column=3)
        ctk.CTkLabel(
            self.game_overview,
            text=f"First to {legs_to_win} legs",
            font=ctk.CTkFont(size=int(self.score_size * 0.3)),
        ).grid(row=2, column=1, columnspan=3)

        # Place elements
        self.label_name_p1.grid(row=11, column=11, padx=10)
        self.label_name_board.grid(row=11, column=21)
        self.label_name_p2.grid(row=11, column=31, padx=10)

        self.label_score_p1.grid(row=21, column=11)
        self.game_overview.grid(row=21, column=21)
        self.label_score_p2.grid(row=21, column=31)

        # Loop
        # self.loop()

    def loop(self):
        self.score_p1.set(self.score_p1.get() - 60)
        self.score_p2.set(self.score_p1.get() - 55)
        self.after(5000, self.loop)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        Game(self, "Heim", "Auswärts").pack()


def main():
    app = App()
    app.mainloop()


locale.setlocale(locale.LC_NUMERIC, "C")
if __name__ == "__main__":
    main()
