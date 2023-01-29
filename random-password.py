import tkinter as tk
import random
import string
import os

def generate_password():
    letters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letters) for i in range(16))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    with open("passwords.txt", "a") as f:
        f.write(f"{website},{username},{password}\n")

root = tk.Tk()
root.title("Password Save Tool")

website_label = tk.Label(root, text="Website:")
website_label.grid(row=0, column=0)
website_entry = tk.Entry(root)
website_entry.grid(row=0, column=1)

username_label = tk.Label(root, text="Username:")
username_label.grid(row=1, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1)

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.grid(row=2, column=2)

save_button = tk.Button(root, text="Save", command=save_password)
save_button.grid(row=3, column=1)

root.mainloop()
