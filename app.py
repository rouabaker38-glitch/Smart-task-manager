tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i + 1}. {task['title']} - {status}")

def add_task():
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    print("Task added!")
  def mark_done():
    show_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        tasks[index]["done"] = True
        print("Task marked as done!")
    except:
        print("Invalid input!")

def delete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        print("Task deleted!")
    except:
        print("Invalid input!")
      while True:
    print("\n-- Smart Task Manager —")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
