# python list

to_do_list = []

# welcome message

def display_welcome_message():
    print("Welcome to the To-Do Application!")
    print("Please choose an option:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Quit")

# functions

def add_task(task):
    try:
        cleaned = task.strip()
        to_do_list.append(cleaned)
        print(f"'{cleaned}' added successfully.", flush=True)
        return True
    except Exception as e:
        print(f"Error adding task: {e}", flush=True)
        return False

def remove_task(task):
    try:
        cleaned = task.strip()
        to_do_list.remove(cleaned)
        print(f"'{cleaned}' removed successfully.", flush=True)
        return True
    except ValueError:
        print(f"Task not found: '{task}'.", flush=True)
        return False

def view_tasks():
    if not to_do_list: 
        print("No tasks.")
    else:
        for task in to_do_list:
            print(f"- {task}")

def quit_application():
    print("Quitting the application...")

def savetasks():
    # Placeholder for saving tasks to persistent storage (not implemented)
    pass

# main loop
try:
    while True:
        display_welcome_message()
        user_choice = input("Enter the number of your choice: ").strip()
        if user_choice == "1":
            task = input("Enter the task you want to add: ").strip()
            add_task(task)
        elif user_choice == "2":
            task = input("Enter the task you want to remove: ").strip()
            remove_task(task)
        elif user_choice == "3":
            view_tasks()
        elif user_choice == "4":
            quit_application()
            break
        else:
            print("Invalid choice. Please try again.", flush=True)
except KeyboardInterrupt:
    print("\nApplication interrupted. Quitting...")
    quit_application()
finally:
    savetasks()