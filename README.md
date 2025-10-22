# python-cli-todo
Persistent Console-based To-Do Manager built with Python. Demonstrates file handling, list manipulation, and context managers for data persistence

## 🎯 Project Objective
To implement a simple, robust, and persistent To-Do List manager using pure Python. The application is designed to run entirely within a terminal environment, utilizing file handling for long-term data storage.

## ✨ Technical Features & Functionality
The application satisfies all core requirements, providing a seamless user experience via the Command Line Interface (CLI):

* **Data Persistence:** Tasks are loaded from and saved to a dedicated text file (`tasks.txt`), ensuring tasks are maintained across different sessions.
* **Core CRUD Operations:** Implements essential features:
    * **Add Task:** Prompts for and adds a new task (using `list.append()`).
    * **View List:** Displays all current tasks with proper indexing.
    * **Remove Task:** Removes a task based on its user-provided index (using `list.pop()`).
* **Enhanced Status Tracking (in todo_enhanced.py):** Includes logic to toggle task status between **Pending** (`[ ]`) and **Done** (`[X]`).

## 💻 Key Concepts Implemented
The solution directly addresses the key concepts and hints provided in the task specification:

| Concept | Implementation Detail |
| :--- | :--- |
| **File Handling** | Used Python's built-in `open()` function with explicit file modes (`'r'` and `'w'`). |
| **Context Managers** | Leveraged the `with open(...)` statement to ensure files are **always closed automatically**, preventing resource leaks. |
| **Lists** | Tasks are managed efficiently in an ordered sequence using Python lists, which serve as the primary **data structure** for in-memory storage. |
| **String Manipulation** | Employed the essential `.strip()` method to clean input and remove extraneous newline characters (`\n`) from file lines, ensuring data integrity. |

## 🚀 Execution Instructions
1.  Ensure you have a modern Python 3 interpreter installed.
2.  Save the code as `todo.py` (or `todo_enhanced.py`).
3.  Execute the application from your Linux or VS Code terminal:
    ```bash
    python3 todo.py
    ```
