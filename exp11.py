import tkinter as tk

# Function to handle button clicks
def on_click(button_text):
    current_text = entry_var.get() 
    if button_text == "=":
        try:
            # Evaluate the expression and update the entry
            result = str(eval(current_text))
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")   
    elif button_text == "C":
        # Clear the entry field
        entry_var.set("")
    else:
        # Append the clicked button text to the entry field
        entry_var.set(current_text + button_text)
# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="#f0f0f0")
# Entry field for displaying input and results
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), justify='right', bd=8, relief=tk.GROOVE)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# Define button labels
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]
# Create buttons and add them to the grid
for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        button = tk.Button(root, text=text, font=("Arial", 20), width=5, height=2,
                           bg="#e0e0e0", fg="#333",
                           command=lambda t=text: on_click(t))
        button.grid(row=r + 1, column=c, padx=5, pady=5)
# Run the Tkinter event loop
root.mainloop()