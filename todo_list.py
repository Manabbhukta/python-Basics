# Simple To-Do List App

tasks = []  # List to store all tasks

def show_tasks():
    print("\n--- Your To-Do List")
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"'{task}' added to the list")

def delete_task():
    show_tasks()
    if len(tasks) > 0:
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"'{removed}' deleted")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

# Main Menu Loop
while True:
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice ='1':
        show_tasks()
    elif choice ='2':
        add_task()
    elif choice ='3':
        delete_task()
    elif choice == '4':
        print("Goodbye! Complete your tasks")
        break
    else:
        print("Invalid Option! Please choose 1-4")
