# Daniel Graham
# Date: 7/12/25
# Module 10.2 Assignment: GUI Todo

import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        self.tasks = tasks if tasks else []

        self.title("Graham To-Do")
        self.geometry("300x400")

        #Menu Bar Added by Daniel Graham!
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu_bar)


        self.tasks_canvas = tk.Canvas(self, bg="white")
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.tasks_frame = tk.Frame(self.tasks_canvas, bg="white")
        self.text_frame = tk.Frame(self)

        # Embed the frame into the canvas
        self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="nw")

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        self.task_create.focus_set()

        # Layout widgets
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Sample initial task
        todo1 = tk.Label(self.tasks_frame, text="Type to Add Items, Right Click to Delete!", bg="orange", fg="black", pady=10)
        todo1.bind("<Button-1>", self.remove_task)
        todo1.pack(side=tk.TOP, fill=tk.X)
        self.tasks.append(todo1)

        for task in self.tasks[1:]:  # already packed todo1
            task.pack(side=tk.TOP, fill=tk.X)

        # Event bindings
        self.bind("<Return>", self.add_task)
        self.tasks_canvas.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)

        self.colour_schemes = [{"bg": "pink", "fg": "black"},
                               {"bg": "red", "fg": "white"}]

    def add_task(self, event=None):
        task_text = self.task_create.get("1.0", tk.END).strip()
        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.set_task_colour(len(self.tasks), new_task)

            new_task.bind("<Button-3>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)
            self.task_create.delete("1.0", tk.END)
            self.on_frame_configure()

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", f"Delete '{task.cget('text')}'?"):
            self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()
            self.on_frame_configure()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)
        scheme = self.colour_schemes[task_style_choice]
        task.configure(bg=scheme["bg"], fg=scheme["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            move = 1 if event.num == 5 else -1
            self.tasks_canvas.yview_scroll(move, "units")

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()