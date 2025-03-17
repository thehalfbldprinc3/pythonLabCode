import tkinter as tk

def on_click(button_text):
    current_text = entry_var.get()
    if button_text == "=":
        try:
            result = str(eval(current_text))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + button_text)

root = tk.Tk()
root.title("Simple Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify='right', bd=10, relief=tk.GROOVE)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        button = tk.Button(root, text=text, font=("Arial", 20), width=5, height=2,
                           command=lambda t=text: on_click(t))
        button.grid(row=r + 1, column=c)

root.mainloop()
