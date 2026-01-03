import json
from datetime import datetime

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    title = input("Enter task title: ")
    priority = input("Enter priority (High / Medium / Low): ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")

    task = {
        "title": title,
        "priority": priority,
        "deadline": deadline,
        "status": "Pending"
    }

    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully!")

# View tasks
def view_tasks(filter_status=None):
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks):
        if filter_status and task["status"] != filter_status:
            continue

        print(f"""
Task ID: {index}
Title: {task['title']}
Priority: {task['priority']}
Deadline: {task['deadline']}
Status: {task['status']}
        """)

# Update task status
def update_task():
    view_tasks()
    task_id = int(input("Enter Task ID to mark as completed: "))

    if 0 <= task_id < len(tasks):
        tasks[task_id]["status"] = "Completed"
        save_tasks(tasks)
        print("✅ Task updated successfully!")
    else:
        print("❌ Invalid Task ID")

# Main menu
tasks = load_tasks()

while True:
    print("""
📋 TASK MANAGEMENT SYSTEM
1. Add Task
2. View All Tasks
3. View Pending Tasks
4. View Completed Tasks
5. Mark Task as Completed
6. Exit
    """)

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks("Pending")
    elif choice == "4":
        view_tasks("Completed")
    elif choice == "5":
        update_task()
    elif choice == "6":
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")
