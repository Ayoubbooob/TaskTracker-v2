import json
TASKS_FILE = 'data.json' #TODO Add file path later 
def load_data():
        try:
            with open(TASKS_FILE, "r") as f:
                tasks = json.load(f)
                return [(task["title"], task["description"])for task in tasks]
        except FileNotFoundError:
            return []

def save_tasks(tasks):
        tasks_data = [{
             "title": task.title, 
             "description": task.description, 
            #  "completedAt": task.completedAt.strftime("%Y-%m-%d %H:%M:%S") if task.completedAt else None} 
            }for task in tasks] 
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks_data, f, indent=4)

# def update_time():
#     current_date = datetime.now()
#     formatted_date = current_date.strftime("%Y-%m-%d %H:%M")

#     return formatted_date
