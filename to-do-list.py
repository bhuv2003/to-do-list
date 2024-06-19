import tkinter as tk
from tkinter import messagebox

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Main window setup
root = tk.Tk()
root.title("To-Do List")

# Frame for task input
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Entry widget for task input
task_entry = tk.Entry(input_frame, font=('Arial', 14), width=30)
task_entry.pack(side=tk.LEFT, padx=10)

# Add Task button
add_button = tk.Button(input_frame, text="Add Task", font=('Arial', 14), command=add_task)
add_button.pack(side=tk.LEFT)

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, font=('Arial', 14), width=45, height=10, selectmode=tk.SINGLE)
tasks_listbox.pack(pady=10)

# Frame for action buttons
action_frame = tk.Frame(root)
action_frame.pack(pady=10)

# Delete Task button
delete_button = tk.Button(action_frame, text="Delete Task", font=('Arial', 14), command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

# Run the main event loop
root.mainloop()
