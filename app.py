def show_menu():
    print("\n--- To-Do List App ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\nYour tasks:")
        for i, (task, done) in enumerate(tasks, 1):
            status = "✓" if done else "✗"
            print(f"{i}. [{status}] {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append((task, False))
    print(f"Added task: {task}")

def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the number of the task to mark as done: "))
        if 1 <= task_num <= len(tasks):
            task, _ = tasks[task_num - 1]
            tasks[task_num - 1] = (task, True)
            print(f"Marked task {task_num} as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()def show_menu():
    print("\n--- To-Do List App ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\nYour tasks:")
        for i, (task, done) in enumerate(tasks, 1):
            status = "✓" if done else "✗"
            print(f"{i}. [{status}] {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append((task, False))
    print(f"Added task: {task}")

def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the number of the task to mark as done: "))
        if 1 <= task_num <= len(tasks):
            task, _ = tasks[task_num - 1]
            tasks[task_num - 1] = (task, True)
            print(f"Marked task {task_num} as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()