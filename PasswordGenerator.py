import random
import string
import tkinter as tk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def show_password():
    password = generate_password(10)
    password_label.config(text=password)

window = tk.Tk()

window.geometry("550x350")
window.configure(background="#72f2e1")

generate_button = tk.Button(window, text="Generate Password", command=show_password,height=3, width=15, background="#fcd492")
generate_button.pack()

password_label = tk.Label(window, text="Password is...")
password_label.pack()

window.mainloop()
