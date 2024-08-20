import tkinter as tk
from tkinter import messagebox
import random

def play_round(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
        update_score(True)
    else:
        result = "You lose!"
        update_score(False)

    messagebox.showinfo("Result", f"Computer chose {computer_choice}.\n{result}")

def update_score(user_won):
    global user_score, computer_score
    if user_won:
        user_score += 1
    else:
        computer_score += 1

    label_score.config(text=f"Score: You {user_score} - {computer_score} Computer")

user_score = 0
computer_score = 0

root = tk.Tk()
root.title("Rock-Paper-Scissors")

tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 16)).pack(pady=10)

tk.Button(root, text="Rock", command=lambda: play_round('Rock')).pack(pady=5)
tk.Button(root, text="Paper", command=lambda: play_round('Paper')).pack(pady=5)
tk.Button(root, text="Scissors", command=lambda: play_round('Scissors')).pack(pady=5)

label_score = tk.Label(root, text=f"Score: You {user_score} - {computer_score} Computer", font=("Helvetica", 12))
label_score.pack(pady=10)


root.mainloop()
