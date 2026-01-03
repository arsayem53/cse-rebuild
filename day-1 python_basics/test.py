def add_task(tasks_list):
    total = int(input("How many tasks do you want to input: "))
    a = 1
    while a <= total:
        work = input(f"Enter task title for #{a}: ")
        new_entry = {
            "task_number": a, 
            "title": work, 
            "status": "incomplete"
        }
        tasks_list.append(new_entry)
        a += 1
    
    return tasks_list

def display_task(task_list, complete_tasks):
    print("Incompleted Tasks Are: ")
    for t in task_list:
        print(f"{t['task_number']}. {t['title']} [{t['status']}]")
    print("Completed Tasks Are: ")
    for t in complete_tasks:
        print(f"{t['task_number']}. {t['title']} [{t['status']}]")

def mark_complete(task_list, complete_tasks):
    target_title = input("Which task is completed: ")
    found = False 
    for task in task_list:
        if task["title"] == target_title:
            task["status"] = "complete"
            complete_tasks.append(task)
            print(f"Success! '{target_title}' moved to completed.")
            task_list.remove(task)
            found = True
            break 
    
    if not found:
        print("Task not found.")
    
    return task_list, complete_tasks

def delete_task(task_list):
    target_title = input("Which task is completed: ")
    found = False 
    for task in task_list:
        if task["title"] == target_title:
            task_list.remove(task)
            found = True
            break 
    
    if not found:
        print("Task not found.")
    
    return task_list
my_tasks = [] 
completed_tasks = []

while True:
    print("""=== TO-DO LIST MANAGER ===
    1. Add task
    2. View all tasks
    3. Mark task as complete
    4. Delete task
    5. Exit""")
    choice = int(input("Choose option (1-5):"))
 
    if choice == 5:
       exit()

    elif choice == 1:
       add_task(my_tasks)

    elif choice == 2:
       display_task(my_tasks, completed_tasks)

    elif choice == 3:
       mark_complete(my_tasks, completed_tasks)

    elif choice == 4:
       delete_task(my_tasks)

