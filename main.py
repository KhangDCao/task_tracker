import sys
import json
import datetime

def task_tracker():
    tasks = load_tasks()
    if len(command) < 2:
        print("Please type something.")
    elif command[1] == 'add' and len(command) == 3:
        add(command[2], tasks)
    elif command[1] == 'update' and len(command) == 4: 
        update(command[2], command[3], tasks)
    elif command[1] == 'delete' and len(command) == 3:
        delete(command[2], tasks)
    elif command[1] == 'mark-in-progress' and len(command) == 3:
        mark_in_progress(command[2], tasks)
    elif command[1] == 'mark-done' and  len(command) == 3:
        mark_done(command[2], tasks)
    elif command[1] == 'list': 
        if len(command) == 2:
            list_all(tasks)
        elif len(command) > 3: 
            print("Wrong syntax. Try again.")
        elif command[2] == 'done':
            list_done(tasks)
        elif command[2] == 'todo': 
            list_todo(tasks)
        elif command[2] == 'in-progress': 
            list_in_progress(tasks)
        else: 
            print("Wrong syntax. Try again.")
    else: 
        print("Wrong syntax. Try again.")
    save_tasks(tasks)
# ------------------HELPER FUNCTION-------------------------
def load_tasks():
    try: 
        with open("tasks.json", "r") as file:
            # turn it into something workable
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=5)

def validate_id(id):
    """return a boolean value, True if id is an interger"""
    try:
        int(id)
        return True
    except ValueError:
        return False

#-------------------CRUD-----------------------------------
def add(description, tasks): 
    """add a new task"""
    new_id = 1 if len(tasks)<1 else max(task["id"] for task in tasks) + 1 
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.datetime.now().isoformat(),
        "updatedAt": datetime.datetime.now().isoformat()
    }
    tasks.append(new_task)
    print(f"Task added successfully (ID: {new_task['id']})")
    return

def update(id, description, tasks):
    """update a task by id"""
    if not validate_id(id):
        print("ID must be a number.")
        return
    for task in tasks:
        if task["id"] == int(id):
            task["description"] = description
            task["updatedAt"] = datetime.datetime.now().isoformat()
            return
    print("No task found to update.")
    return
    
def delete(id, tasks):
    """delete a task by id"""
    if not validate_id(id):
            print("ID must be a number.")
            return
    for index, task in enumerate(tasks):
        if task["id"] == int(id):
            tasks.pop(index)
            return
    print("No task found to delete.")
    return

#-----------------MARKING A TASK AS DONE OR IN PROGRESS----------
def mark_in_progress(id, tasks):
    """change task's status."""
    if not validate_id(id):
            print("ID must be a number.")
            return
    for task in tasks: 
        if task["id"] == int(id):
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.datetime.now().isoformat()
            return
    print("No task found to mark.")
    return

def mark_done(id, tasks):
    """mark a task status as done"""
    if not validate_id(id):
            print("ID must be a number.")
            return
    for task in tasks:
        if task["id"] == int(id):
            task["status"] = "done"
            task["updatedAt"] = datetime.datetime.now().isoformat()
            return
    print("No task found to mark.")
    return

# ----------------LIST TASKS-------------------------------------
def list_all(tasks):
    """list all tasks"""
    print(tasks)
    return

def list_done(tasks): 
    """list all done tasks"""
    for task in tasks: 
        if task["status"] == "done":
            print(task)
    return
    
def list_todo(tasks):
    """list all tasks that are not done"""
    for task in tasks:
        if task["status"] == "todo":
            print(task)
    return

def list_in_progress(tasks):
    """list all tasks that are in progress"""
    for task in tasks:
        if task["status"] == "in-progress":
            print(task)
    return

command = sys.argv

task_tracker()