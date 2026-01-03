def add_task(tasks):
      task_number = input("How many task you want to input: ")
      while True:
        a = 1
        if a <= task_number:
            work = input("Enter task title: ")
            tasks = {
                "Task number" : a, "Task title: " : work, "status:" : "incompleted"
            }
      return tasks
def view_task():
    for key, values in tasks.items():
        print(f"Task no: {key}  is {values}")

def mark_complete(tasks, cmp_tasks):
    complete = input("Mark complete task: ")
    if complete in tasks:
        tasks[complete] = cmp_tasks[complete]
        del tasks[complete]
        return tasks, cmp_tasks
    else:
        print("Wrong value")   
    print(f"Remaining tasks: {tasks}")
def delete_task():
    delete = input("Deleted task: ")
    if delete in tasks:
        del tasks[delete]

tasks = {}
cmp_tasks = {}
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
       add_task(tasks)

    elif choice == 2:
       view_task()

    elif choice == 3:
       mark_complete(tasks, cmp_tasks)

    elif choice == 4:
       delete_task()

