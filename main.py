import tkinter as tk
from tkinter import ttk


def insert_value(valor):
    entry.insert(tk.END, valor)

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END) 
        entry.insert(tk.END, str(result))  
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

def limpar():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

entry = ttk.Entry(root, font=("Arial", 24), justify="center")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3)
]

for (text, line, column) in buttons:
    if text == "=":
        btn = ttk.Button(root, text=text, command=calculate)

    else:
        btn = ttk.Button(root, text=text, command=lambda t=text: insert_value(t))
    btn.grid(row=line, column=column, padx=10, pady=10, ipadx=10, ipady=10)

btn_clear = ttk.Button(root, text="C", command=limpar)
btn_clear.grid(row=0, column=3, padx=10, pady=10, ipadx=10, ipady=10)


root.mainloop()