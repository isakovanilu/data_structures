"""
Todo List: Create a simple command-line 
to-do list application where users can add tasks, 
view all tasks, and delete a task. 
This will introduce arrays or arraylists and the basics of 
CRUD (Create, Read, Update, Delete) operations.
"""
class ToDoList():
    def __init__(self, todo_lists=None):        
        if todo_lists is None:
            todo_lists = []
        self.todo_lists = todo_lists
        

        