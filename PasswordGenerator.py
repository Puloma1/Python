import random
import string
import tkinter as tk

def generate_password(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use the random.choice function to select characters for the password
    password = ''.join(random.choice(characters) for i in range(length))

    return password

def show_password():
    password = generate_password(10)
    password_label.config(text=password)

# Create a window
window = tk.Tk()

# Add a button that will call show_password when clicked
generate_button = tk.Button(window, text="Generate Password", command=show_password,height=3, width=15, background="#fcd492")
generate_button.pack()


# Add a label to display the generated password
password_label = tk.Label(window, text="Password is...")
password_label.pack()


window.geometry("550x350")
window.configure(background="#72f2e1")

# Start the GUI event loop
window.mainloop()
