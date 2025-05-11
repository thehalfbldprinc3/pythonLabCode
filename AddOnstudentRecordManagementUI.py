import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import pandas as pd
import os

FILENAME = "students.csv"

# Ensure the file exists with correct headers
def initialize_file():
    if not os.path.exists(FILENAME):
        df = pd.DataFrame(columns=["Roll No", "Name", "Age", "Branch"])
        df.to_csv(FILENAME, index=False)

def add_student(roll, name, age, branch):
    df = pd.read_csv(FILENAME)
    if str(roll) in df["Roll No"].astype(str).values:
        return False
    df.loc[len(df.index)] = [roll, name, age, branch]
    df.to_csv(FILENAME, index=False)
    return True

def get_all_students():
    return pd.read_csv(FILENAME)

def search_student(roll):
    df = pd.read_csv(FILENAME)
    result = df[df["Roll No"] == roll]
    return result if not result.empty else None

def update_student(roll, name, age, branch):
    df = pd.read_csv(FILENAME)
    if roll not in df["Roll No"].values:
        return False
    df.loc[df["Roll No"] == roll] = [roll, name, age, branch]
    df.to_csv(FILENAME, index=False)
    return True

def delete_student(roll):
    df = pd.read_csv(FILENAME)
    df = df[df["Roll No"] != roll]
    df.to_csv(FILENAME, index=False)

# GUI
class StudentGUI:
    def __init__(self, master):
        self.master = master
        master.title("Student Management System")
        master.geometry("400x400")
        
        tk.Button(master, text="Add Student", width=25, command=self.add_student_window).pack(pady=5)
        tk.Button(master, text="View All Students", width=25, command=self.view_students).pack(pady=5)
        tk.Button(master, text="Search Student", width=25, command=self.search_student_window).pack(pady=5)
        tk.Button(master, text="Update Student", width=25, command=self.update_student_window).pack(pady=5)
        tk.Button(master, text="Delete Student", width=25, command=self.delete_student_window).pack(pady=5)
        tk.Button(master, text="Exit", width=25, command=master.quit).pack(pady=20)

    def add_student_window(self):
        self.input_window("Add Student", self.add_student_action)

    def update_student_window(self):
        self.input_window("Update Student", self.update_student_action)

    def input_window(self, title, action):
        win = tk.Toplevel(self.master)
        win.title(title)

        labels = ["Roll No", "Name", "Age", "Branch"]
        entries = []

        for label in labels:
            tk.Label(win, text=label).pack()
            entry = tk.Entry(win)
            entry.pack()
            entries.append(entry)

        def on_submit():
            values = [e.get().strip() for e in entries]
            if "" in values:
                messagebox.showerror("Error", "All fields are required.")
                return
            try:
                roll = int(values[0])
                age = int(values[2])
            except:
                messagebox.showerror("Error", "Roll No and Age must be integers.")
                return
            action(roll, values[1], age, values[3])
            win.destroy()

        tk.Button(win, text="Submit", command=on_submit).pack(pady=5)

    def add_student_action(self, roll, name, age, branch):
        if add_student(roll, name, age, branch):
            messagebox.showinfo("Success", "Student added successfully.")
        else:
            messagebox.showerror("Error", "Roll No already exists.")

    def update_student_action(self, roll, name, age, branch):
        if update_student(roll, name, age, branch):
            messagebox.showinfo("Success", "Student updated successfully.")
        else:
            messagebox.showerror("Error", "Student not found.")

    def view_students(self):
        data = get_all_students()
        self.display_table(data)

    def search_student_window(self):
        roll = simpledialog.askinteger("Search Student", "Enter Roll No:")
        if roll is not None:
            result = search_student(roll)
            if result is not None:
                self.display_table(result)
            else:
                messagebox.showinfo("Result", "Student not found.")

    def delete_student_window(self):
        roll = simpledialog.askinteger("Delete Student", "Enter Roll No:")
        if roll is not None:
            delete_student(roll)
            messagebox.showinfo("Success", "Student deleted (if existed).")

    def display_table(self, df):
        win = tk.Toplevel(self.master)
        win.title("Student Records")
        tree = ttk.Treeview(win)
        tree["columns"] = list(df.columns)
        tree["show"] = "headings"
        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, anchor=tk.CENTER)
        for i in df.values.tolist():
            tree.insert("", "end", values=i)
        tree.pack(expand=True, fill="both")

# Main
if __name__ == "__main__":
    initialize_file()
    root = tk.Tk()
    app = StudentGUI(root)
    root.mainloop()