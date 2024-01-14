import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        # Task Entry
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Add Task Button
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        # Listbox to Display Tasks
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40)
        self.task_listbox.pack(pady=10)

        # Delete Task Button
        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            confirmation = messagebox.askokcancel("Confirmation", f"Do you want to delete the task: {task}?")
            if confirmation:
                del self.tasks[selected_index[0]]
                self.task_listbox.delete(selected_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
