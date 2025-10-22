import tkinter as tk
import random

class NumGuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("NumGuess")
        self.root.geometry("300x250")
        self.root.resizable(False, False)

        self.secret_number = random.randint(1, 250)
        self.tries = 0

        tk.Label(root, text="Suggest the number from 1 to 250", font=("Arial", 12, "bold"))

        self.entry = tk.Entry(root, justify="center", font=("Arial", 12))
        self.entry.pack(pady=5)
        self.entry.focus()

        self.entry.bind("<Return>", lambda event: self.check_guess())

        tk.Button(root, text="Try", command=self.check_guess, bg="#4CAF50").pack(pady=5)
        tk.Button(root, text="New game", command=self.reset_game, bg="#2196F3").pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 11))
        self.result_label.pack(pady=10)

        self.tries_label = tk.Label(root, text="Guesses: 0", font=("Arial", 10, "italic"))
        self.tries_label.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="Please enter a number!", fg="red")

        self.tries += 1
        self.tries_label.config(text=f"Guesses: {self.tries}")

        if guess < self.secret_number:
            self.result_label.config(text="Too low!", fg="orange")
        elif guess > self.secret_number:
            self.result_label.config(text="Too big!", fg="orange")
        else:
            self.result_label.config(text=f"Correct! The number was: {self.secret_number}.", fg="green")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.tries = 0
        self.result_label.config(text="")
        self.tries_label.config(text="Versuche: 0")
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = NumGuessGame(root)
    root.mainloop()