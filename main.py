from task import Task
from utils import load_data, save_tasks, update_time
def create_task(tasks):
    title= input("-----Enter the title: ")

    description = input("Enter the description: ")
    # completedAt = update_time()
    new_task = Task(title, description)
    tasks.append(new_task)
    save_tasks(tasks)

    print("Task added successfully!")


def list_tasks(tasks):
    print("Tasks: ")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}: {task}")
    print()

def mark_complete(tasks):
    list_tasks(tasks)
    try:
        idx= int(input("Enter the index of the task to mark as complete: ")) - 1
        tasks[idx].mark_complete()
        save_tasks(tasks)
    except (ValueError, IndexError):
        print("Invalid input. PLease enter a valid task index.")
def main():
    tasks = load_data()

    while True:
        print("Task Manager")
        print("1. Add Task")
        print("2- List Taks")
        print("3- Mark Task as complete")
        print("4- Quit")

        choice= input("Select an option: ")

        if choice == "1":
            create_task(tasks)
            
        elif choice == "2":
            list_tasks(tasks)
            
        elif choice == "3":
            mark_complete(tasks)
            
        elif choice == "4":
            break
        else:
            print("Ivalid choice. Please select a valid option.")


if  __name__== "__main__":
    main()