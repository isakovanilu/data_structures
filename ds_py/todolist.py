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
        
    def add_task(self, task):
        self.todos.append(task)
        
    def delete_by_index(self, index):
        if len(self.todos) == 0:
            print('List is empty')
        self.todos.remove(self.todos[index])

    def delete_todo(self, todo):
        if self.todos == []:
            print('List is empty')
        self.todos.remove(todo)
        
    def view(self):
        todo = [print(todo) for todo in self.todos]
        return todo