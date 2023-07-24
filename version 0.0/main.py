import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def button_click(value):
    if value == "=":
        calculate()
    else:
        entry.insert(tk.END, str(value))

def clear():
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")
window.resizable(False, False)
window.configure(bg="#E6F5FF")



icon16 = Image.open("icon16x16.ico")
icon32 = Image.open("icon32x32.ico")
icon48 = Image.open("icon48x48.ico")
icon256 = Image.open("icon256x256.ico")



window.iconphoto(True, ImageTk.PhotoImage(icon16))
window.iconbitmap(r"icon32x32.ico")

entry = tk.Entry(window, width=25, font=("Arial", 20), bd=0, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
entry.focus_set()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

row_index = 1
col_index = 0
for button in buttons:
    if col_index > 3:
        col_index = 0
        row_index += 1

    btn = tk.Button(window, text=button, width=5, height=2, bg='#ADD8E6', fg='white',
                    font=("Arial", 16, "bold"), bd=0,
                    command=lambda value=button: button_click(value))
    btn.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")
    window.grid_columnconfigure(col_index, weight=1)  # Make column expandable
    col_index += 1

clear_btn = tk.Button(window, text="C", width=5, height=2, bg='#FFB6C1', fg='white',
                      font=("Arial", 16, "bold"), bd=0, command=clear)
clear_btn.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")
window.grid_columnconfigure(col_index, weight=1)  # Make column expandable

equal_btn = tk.Button(window, text="=", width=5, height=2, bg='#FFB6C1', fg='white',
                      font=("Arial", 16, "bold"), bd=0, command=calculate)
equal_btn.grid(row=row_index+1, column=col_index, padx=5, pady=5, sticky="nsew")
window.grid_columnconfigure(col_index, weight=1)  # Make column expandable

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)

window.bind('<Return>', lambda event: calculate())

window.mainloop()
