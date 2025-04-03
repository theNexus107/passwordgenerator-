import random
import tkinter as tk

def generate_password():
    try:
        length = int(length_entry.get())  
        if length < 1:
            password_var.set("Length must be greater than 0")
            return
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#*&"
        password = ""
        
        for i in range(length):  
            password += random.choice(characters)
        
        password_var.set(password)  
    except ValueError:
        password_var.set("Enter a valid number")


root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")


tk.Label(root, text="Enter Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)


password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=("Arial", 14))
password_label.pack(pady=10)


root.mainloop()
