import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation based on the chosen operation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation selected.")
            return
        
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place widgets
tk.Label(root, text="Number 1:").grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

tk.Label(root, text="Number 2:").grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

tk.Label(root, text="Operation:").grid(row=2, column=0)
operation_var = tk.StringVar(value='+')
tk.OptionMenu(root, operation_var, '+', '-', '*', '/').grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, columnspan=2)

label_result = tk.Label(root, text="Result:")
label_result.grid(row=4, columnspan=2)

# Run the application
root.mainloop()
