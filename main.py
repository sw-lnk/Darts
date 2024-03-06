import tkinter as tk
import ttkbootstrap as ttk
import customtkinter as ctk

import locale


class Darts(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window title
        self.title("Darts")


def main():
    app = Darts()
    app.mainloop()


locale.setlocale(locale.LC_NUMERIC, "C")
if __name__ == "__main__":
    main()
