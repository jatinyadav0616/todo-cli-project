# todo_cli.py
# A simple CLI To-Do List app in Python

def display_menu():
    print("\n==== TO-DO LIST ====")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Delete Task")
    print("4. Show Tasks")
    print("5. Exit")

def load_tasks(filename="tasks.txt"):
    tasks = []
    try:
        with open(filename, "r") as file:
            for line in file:
                title, status = line.strip().split("|")
                tasks.append({"title": title, "done": status == "✓"})
    except FileNotFoundError:
        pass  # If file doesn't exist, return empty list
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            status = "✓" if task["done"] else "✗"
            file.write(f"{task['title']}|{status}\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. {task['title']} [{status}]")

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter task: ")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
        elif choice == "2":
            show_tasks(tasks)
            num = int(input("Enter task number to mark complete: "))
            if 0 < num <= len(tasks):
                tasks[num-1]["done"] = True
                save_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            num = int(input("Enter task number to delete: "))
            if 0 < num <= len(tasks):
                del tasks[num-1]
                save_tasks(tasks)
        elif choice == "4":
            show_tasks(tasks)
        elif choice == "5":
            print("Exiting...")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
