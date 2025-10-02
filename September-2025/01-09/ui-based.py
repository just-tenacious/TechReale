import tkinter as tk
from tkinter import messagebox, ttk
from connect import connection   # ✅ using your pymysql connection

cursor = connection.cursor()

# ----------------- Create Table if not exists -----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT
)
""")

# ----------------- Functions -----------------
def insert_user():
    name = entry_name.get().strip()
    age = entry_age.get()

    if name == "" or not age.isdigit() or not (1 <= int(age) <= 100):
        messagebox.showerror("Error", "Enter valid name and age (1-100).")
        return

    try:
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, int(age)))
        connection.commit()
        messagebox.showinfo("Success", "User added successfully!")
        view_users()
        clear_inputs()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def view_users():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

def update_user():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select a user to update.")
        return

    values = tree.item(selected, "values")
    user_id = values[0]
    name = entry_name.get().strip()
    age = entry_age.get()

    if name == "" or not age.isdigit() or not (1 <= int(age) <= 100):
        messagebox.showerror("Error", "Enter valid name and age (1-100).")
        return

    try:
        cursor.execute("UPDATE users SET name=%s, age=%s WHERE id=%s", (name, int(age), user_id))
        connection.commit()
        messagebox.showinfo("Success", "User updated successfully!")
        view_users()
        clear_inputs()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_user():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select a user to delete.")
        return

    values = tree.item(selected, "values")
    user_id = values[0]

    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this user?")
    if confirm:
        try:
            cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
            connection.commit()
            messagebox.showinfo("Success", "User deleted successfully!")
            view_users()
            clear_inputs()
        except Exception as e:
            messagebox.showerror("Error", str(e))

def clear_inputs():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)

def load_selected(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, "values")
        entry_name.delete(0, tk.END)
        entry_name.insert(0, values[1])
        entry_age.delete(0, tk.END)
        entry_age.insert(0, values[2])

# ----------------- UI Setup -----------------
root = tk.Tk()
root.title("User CRUD App (PyMySQL + Tkinter)")
root.geometry("600x400")

# Input Fields
frame_inputs = tk.Frame(root, pady=10)
frame_inputs.pack()

tk.Label(frame_inputs, text="Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_inputs)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Age:").grid(row=1, column=0, padx=5, pady=5)
entry_age = tk.Entry(frame_inputs)
entry_age.grid(row=1, column=1, padx=5, pady=5)

# Buttons
frame_buttons = tk.Frame(root, pady=10)
frame_buttons.pack()

tk.Button(frame_buttons, text="Add User", command=insert_user).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Update User", command=update_user).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Delete User", command=delete_user).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Clear", command=clear_inputs).grid(row=0, column=3, padx=5)

# Table
columns = ("ID", "Name", "Age")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.pack(fill="both", expand=True, pady=10)
tree.bind("<<TreeviewSelect>>", load_selected)

# Load initial data
view_users()

root.mainloop()
