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
        self.todo_lists.append(task)
        
    def delete_by_index(self, index):
        if len(self.todo_lists) == 0:
            print('List is empty')
        self.todo_lists.remove(self.todo_lists[index])
        print('removed')

    def delete_todo(self, todo):
        if self.todo_lists == []:
            print('List is empty')
        self.todo_lists.remove(todo)
        
    def view(self):
        todo = [print(todo) for todo in self.todo_lists]
        return todo
    
