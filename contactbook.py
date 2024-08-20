import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = {}

def add_contact():
    name = simpledialog.askstring("Input", "Enter the contact name:")
    if not name:
        return
    phone = simpledialog.askstring("Input", "Enter the contact phone number:")
    if not phone:
        return
    contacts[name] = phone
    update_contact_list()
    messagebox.showinfo("Success", "Contact added successfully!")

def view_contact():
    name = simpledialog.askstring("Input", "Enter the contact name to view:")
    if not name:
        return
    phone = contacts.get(name)
    if phone:
        messagebox.showinfo("Contact Info", f"Name: {name}\nPhone: {phone}")
    else:
        messagebox.showwarning("Not Found", "Contact not found!")

def delete_contact():
    name = simpledialog.askstring("Input", "Enter the contact name to delete:")
    if not name:
        return
    if name in contacts:
        del contacts[name]
        update_contact_list()
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showwarning("Not Found", "Contact not found!")

def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for name in contacts:
        listbox_contacts.insert(tk.END, name)

root = tk.Tk()
root.title("Contact Book")

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="View Contact", command=view_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

listbox_contacts = tk.Listbox(root, width=50)
listbox_contacts.pack(pady=10)

update_contact_list()  

root.mainloop()
