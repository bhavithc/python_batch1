tasks = []
next_id = 1


def add(task_name, priority):
    global next_id

    tasks.append({
        "id": next_id,
        "task_name": task_name,
        "priority": priority,
        "completed": False
    })

    next_id += 1
    print("Task added successfully.\n")


def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return

    print("\n-------------------------------")
    print("ID\tTask\t\tPriority\tStatus")
    print("-------------------------------")

    for task in tasks:
        status = "Done" if task["completed"] else "Open"

        print(f'{task["id"]}\t{task["task_name"]}\t\t{task["priority"]}\t\t{status}')

    print()


def delete(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task deleted.\n")
            return

    print("Task not found.\n")


def toggle(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            print("Task updated.\n")
            return

    print("Task not found.\n")


def dashboard():
    total = len(tasks)

    completed = 0
    open_tasks = 0

    for task in tasks:
        if task["completed"]:
            completed += 1
        else:
            open_tasks += 1

    print("\n====== Dashboard ======")
    print(f"Total Tasks : {total}")
    print(f"Open Tasks  : {open_tasks}")
    print(f"Completed   : {completed}")
    print("=======================\n")


if __name__ == "__main__":

    while True:

        print("========== TO DO ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Toggle Task")
        print("4. Delete Task")
        print("5. Dashboard")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            task_name = input("Enter task name: ")
            priority = input("Enter priority (High/Medium/Low): ")

            add(task_name, priority)

        elif choice == "2":

            view_tasks()

        elif choice == "3":

            task_id = int(input("Enter Task ID: "))
            toggle(task_id)

        elif choice == "4":

            task_id = int(input("Enter Task ID: "))
            delete(task_id)

        elif choice == "5":

            dashboard()

        elif choice == "6":

            print("Good Bye!")
            break

        else:

            print("Invalid choice.\n")