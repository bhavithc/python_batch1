
tasks = []
next_id = 1

def add(task_name, priority):
    global next_id
    tasks.append({"task_name": task_name, 
     "prority": priority,
     "status": "Open",
     "id": next_id})
    next_id = next_id + 1

def print_all_tasks():
    for task in tasks:
        print(task)

def update(task_id, is_done):
    for task in tasks:
        if task_id == task["id"]:
            if is_done:
                task["status"] = "Close"
            else:
                task["status"] = "Open"
            
            break

def delete(task_id):
    for task in tasks:
        if task_id == task["id"]:
            tasks.remove(task)
            break

def summary():

    total = len(tasks)
    open = 0

    for task in tasks:
        if task["status"] == "Open":
            open += 1

    print("--" * 20)
    print(f"Total tasks: {total}")
    print(f"Open tasks: {open}")
    print(f"Closed tasks: {total - open}")
    print("--" * 20)

if __name__ == "__main__":
    add(task_name="python_program", priority="Medium")
    add(task_name="java_task", priority="High")
    add(task_name="Sacala_task", priority="Low")
    add(task_name="R_task", priority="Medium")


    print_all_tasks()
    update(1, False)
    update(2,True)
    print("--------")
    print_all_tasks()
    delete(1)
    print_all_tasks()
    summary()

    # print(tasks)
    # print(next_id)