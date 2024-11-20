import tkinter as tk
from tkinter import messagebox
import pickle

# Load tasks from file
def load_tasks():
    try:
        with open('tasks.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(tasks, f)

# Add a new task
def add_task():
    task = entry_task.get()
    if task:
        tasks_list.insert(tk.END, task)
        tasks.append({'task': task, 'done': False})
        entry_task.delete(0, tk.END)

# Update a task (mark as done/undone)
def update_task(event):
    selected_task_index = tasks_list.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        tasks[index]['done'] = not tasks[index]['done']
        update_task_display(index)

# Update the display of a specific task based on its done status
def update_task_display(index):
    task = tasks[index]
    task_str = task['task']
    if task['done']:
        task_str += " [✓]"
        tasks_list.itemconfig(index, {'fg': 'gray'})  # Gray color for completed tasks
    else:
        tasks_list.itemconfig(index, {'fg': 'black'})
    tasks_list.delete(index)
    tasks_list.insert(index, task_str)

# Delete a task
def delete_task():
    selected_task_index = tasks_list.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        tasks_list.delete(index)
        tasks.pop(index)

# Save tasks on close confirmation
def on_close():
    if messagebox.askokcancel("Quit", "Do you want to save your tasks before exiting?"):
        save_tasks(tasks)
        root.destroy()


# Setup main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("665x400+550+250")  # Set window size to 600x400 pixels
root.resizable(0, 0)
root.configure(bg="#B5E5CF")


# Entry for new tasks
entry_task = tk.Entry(root, width=50)
entry_task.pack()

# Add Task button
btn_add_task = tk.Button(root, text="Add Task", command=add_task)
btn_add_task.pack()

# Listbox to display tasks
tasks_list = tk.Listbox(root, width=50, height=10)
tasks_list.pack()
tasks_list.bind("<Double-1>", update_task)
tasks_list.bind("<Delete>", lambda event: delete_task())  # Delete task on pressing 'Delete' key

# Delete Task button
btn_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
btn_delete_task.pack()

# Load initial tasks
tasks = load_tasks()
for idx, task in enumerate(tasks):
    task_str = task['task']
    if task['done']:
        task_str += " [✓]"
    tasks_list.insert(tk.END, task_str)
    # Update the task display style based on the done status
    if task['done']:
        tasks_list.itemconfig(idx, {'fg': 'gray'})  # Set color to gray for completed tasks

# Run the main event loop
root.mainloop()
