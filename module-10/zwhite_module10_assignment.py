# =============================================================================
# Name:         Zachary White
# Instructor:   Darrell Payne
# Date:         05/14/2026
# Course:       CSD325
# =============================================================================
# Program:      Zachary's To-Do List Application
# File:         todo_app.py
#
# Description:
#   A simple graphical To-Do List application built using Python's tkinter
#   library. The application allows users to add tasks via a text entry field
#   (or by pressing Enter) and delete tasks by right-clicking them. Tasks are
#   displayed in a scrollable listbox with alternating gold and purple row
#   colors for readability. A File menu provides an Exit option to close the
#   application cleanly.
#
# Classes:
#   ToDoApp(tk.Tk)
#       Main application window. Inherits from tk.Tk so the class itself
#       serves as the root window.
#
# Methods:
#   __init__()       - Initializes the window, task storage list, menu, and UI.
#   _build_menu()    - Creates the top menu bar with a File > Exit option.
#   _build_ui()      - Builds all UI widgets: label, entry field, add button,
#                      scrollable listbox, and scrollbar.
#   add_task()       - Reads the entry field, appends the task to the internal
#                      list and listbox, applies alternating row colors, then
#                      clears the entry field.
#   delete_task(e)   - Detects the nearest listbox item to a right-click event,
#                      removes it from both the listbox and internal list, and
#                      re-applies alternating row colors to remaining items.
#
# Change Log:
#   v1.0  05/14/2026  Zachary White
#         - Initial release.
#         - Implemented ToDoApp class inheriting from tk.Tk.
#         - Added File menu with Exit command using a purple/white color scheme.
#         - Built entry frame with text field and "Add Task" button (gold).
#         - Added scrollable Listbox with alternating gold/purple row coloring.
#         - Bound <Return> key to add_task() for keyboard convenience.
#         - Bound right mouse button (<Button-3>) to delete_task() for removal.
#         - Added re-coloring logic after deletion to keep alternating pattern.
#         - Window set to 400x500, resizable in both directions.
# =============================================================================

import tkinter as tk


class ToDoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Zachary's To Do list")
        self.geometry("400x500")
        self.resizable(True, True)

        # Internal list to track tasks in sync with the Listbox widget
        self.task_list = []

        self._build_menu()
        self._build_ui()

    def _build_menu(self):
        """Build the top menu bar with a File > Exit option."""
        menu_bar = tk.Menu(
            self,
            bg="#9B59B6", fg="white",
            activebackground="#6C3483", activeforeground="white"
        )
        file_menu = tk.Menu(
            menu_bar, tearoff=0,
            bg="#9B59B6", fg="white",
            activebackground="#6C3483", activeforeground="white"
        )
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu_bar)

    def _build_ui(self):
        """Build all main UI components: status label, entry field, and task listbox."""

        # Status / instruction label at the top
        self.task_label = tk.Label(
            self,
            text="Items Added --- ** Right Click Item to Delete **",
            bg="#9B59B6",
            fg="white",
            font=("Arial", 10, "bold"),
            pady=6
        )
        self.task_label.pack(fill=tk.X)

        # Frame holding the text entry and Add Task button side by side
        entry_frame = tk.Frame(self)
        entry_frame.pack(fill=tk.X, padx=10, pady=(10, 0))

        self.task_entry = tk.Entry(entry_frame, font=("Arial", 12))
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        # Allow pressing Enter as a shortcut to add a task
        self.task_entry.bind("<Return>", lambda e: self.add_task())

        add_btn = tk.Button(
            entry_frame, text="Add Task",
            bg="#F1C40F", fg="black", font=("Arial", 10, "bold"),
            command=self.add_task
        )
        add_btn.pack(side=tk.LEFT, padx=(6, 0))

        # Frame holding the Listbox and its vertical scrollbar
        list_frame = tk.Frame(self)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            font=("Arial", 12),
            selectbackground="#9B59B6",
            activestyle="none",
            bg="white",
            fg="black",
            height=15
        )
        self.task_listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.task_listbox.yview)

        # Right-click deletes the item nearest to the cursor
        self.task_listbox.bind("<Button-3>", self.delete_task)

    def add_task(self):
        """Read the entry field and add a non-empty task to the list."""
        task = self.task_entry.get().strip()
        if task:
            self.task_list.append(task)
            self.task_listbox.insert(tk.END, task)

            # Apply alternating row colors: even = gold, odd = purple
            idx = self.task_listbox.size() - 1
            if idx % 2 == 0:
                self.task_listbox.itemconfig(idx, bg="#F1C40F", fg="black")
            else:
                self.task_listbox.itemconfig(idx, bg="#9B59B6", fg="white")

            # Clear the entry field after adding
            self.task_entry.delete(0, tk.END)

    def delete_task(self, event):
        """Delete the task nearest to the right-click position and re-color the list."""
        try:
            index = self.task_listbox.nearest(event.y)
            self.task_listbox.delete(index)
            del self.task_list[index]

            # Re-apply alternating colors after removal to keep pattern consistent
            for i in range(self.task_listbox.size()):
                if i % 2 == 0:
                    self.task_listbox.itemconfig(i, bg="#F1C40F", fg="black")
                else:
                    self.task_listbox.itemconfig(i, bg="#9B59B6", fg="white")
        except Exception:
            pass  # Ignore errors if no item is near the click position


if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()