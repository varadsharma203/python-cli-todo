# todo.py

# The name of the file used for permanent storage of tasks.
TASK_FILE = "tasks.txt"

# --------------------
# 1. FILE HANDLING FUNCTIONS
# --------------------

def load_tasks():
    """Reads tasks from the file and returns them as a list."""
    tasks = []
    try:
        # 'r' mode for reading the file.
        # The 'with open(...)' statement is a context manager, ensuring the file is closed automatically.
        with open(TASK_FILE, 'r') as file:
            for line in file:
                # .strip() removes leading/trailing whitespace and the newline character ('\n').
                tasks.append(line.strip())
    except FileNotFoundError:
        # Handles the case where the file doesn't exist (e.g., first run).
        print(f"'{TASK_FILE}' not found. Starting with an empty To-Do list.")
    return tasks

def save_tasks(tasks):
    """Writes the current list of tasks back to the file."""
    # 'w' mode for writing (overwriting) the file entirely.
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            # Write each task followed by a newline character to keep them on separate lines.
            file.write(task + "\n")

# --------------------
# 2. CORE TO-DO LIST FUNCTIONS
# --------------------

def view_tasks(tasks):
    """Displays the current To-Do list, numbered."""
    if not tasks:
        print("\nYour To-Do list is currently empty! ✅")
        return

    print("\n--- Current To-Do List ---")
    # enumerate() provides both the index (i) and the element (task).
    # We add 1 to 'i' to display user-friendly, 1-based numbering.
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")
    print("--------------------------")

def add_task(tasks):
    """Prompts the user for a new task and adds it to the list."""
    task = input("Enter the new task: ").strip()
    if task:
        # append() adds the element to the end of the list.
        tasks.append(task)
        print(f"Task added: '{task}'")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    """Removes a task based on its number (index + 1) from the list."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        # Get user input for the task number
        task_num_str = input("Enter the number of the task to remove: ")
        
        # Check if input is a digit before converting
        if not task_num_str.isdigit():
            print("Invalid input. Please enter a whole number.")
            return

        task_num = int(task_num_str)
        
        # Convert user-friendly number (1-based) to list index (0-based)
        task_index = task_num - 1

        if 0 <= task_index < len(tasks):
            # pop() removes and returns the element at the specified index.
            removed_task = tasks.pop(task_index)
            print(f"Task removed: '{removed_task}'")
        else:
            print("Invalid task number. Please enter a number from the list.")
            
    except Exception as e:
        # General catch-all for unexpected issues
        print(f"An unexpected error occurred: {e}")

# --------------------
# 3. MAIN APPLICATION LOOP
# --------------------

def main():
    """The main function to run the console-based To-Do application."""
    print("Welcome to the Console To-Do List Application! 📋")
    
    # 1. Load tasks from file at startup
    todo_list = load_tasks()

    while True:
        # Display the main menu
        print("\nOptions:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit and Save")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            view_tasks(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            # 2. Save tasks before exiting to ensure persistence
            save_tasks(todo_list)
            print("Tasks saved successfully. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
