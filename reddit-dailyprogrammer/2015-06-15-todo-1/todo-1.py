# http://www.reddit.com/r/dailyprogrammer/comments/39ws1x/20150615_challenge_218_easy_todo_list_part_1/
class ToDoList:
    
    # Constructor
    def __init__(self):
        self.todos = []
    
    # Add an item to the to-do list
    def add_item(self,item):
        self.todos.append(item)
        
    # Delete a selected item from the to-do list by index
    def delete_item(self,index):
        del self.todos[index]
    
    # Print the list
    def print_list(self):
        for i in range(0,len(self.todos)):
            print str(i) + ":" + self.todos[i]
            
t_list = ToDoList()
# Start the program
while True:
    in_value = raw_input("What do you need to do?\n(a) Add a task\n(d) Delete a task\n(p) Print the task list.\n(e) Exit\n")
    if in_value == "a": # Add an item
        item = raw_input("Describe your task: ")
        t_list.add_item(item)
    elif in_value == "d": # Delete an item
        t_list.print_list()
        item = raw_input("Enter the item of the number you want to delete: ")
        t_list.delete_item(int(item))
    elif in_value == "p": # Print the list
        t_list.print_list()
    if in_value == "e":
        break