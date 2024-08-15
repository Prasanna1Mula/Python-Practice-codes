def show_menu():
    print("To do list menu:")
    print("1. Add task")
    print("2. View task")
    print("3. Mark task as done")
    print("4. Exit")

def add_task(tasks):
    task_name = input("Enter you task name: ")
    tasks.append({"name": task_name, "done": False})
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):status = "Done" if task["done"] else "Not done"
        print(f"{index+1}.{task['name']} - {status}")

def mark_task_done(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter task number to mark as done: ")) -1 
        
