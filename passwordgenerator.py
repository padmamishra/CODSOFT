import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():

    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    label_password.config(text=f"Generated Password: {password}")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Generate Password", command=generate_password).grid(row=1, columnspan=2, padx=10, pady=10)

label_password = tk.Label(root, text="Generated Password:")
label_password.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
