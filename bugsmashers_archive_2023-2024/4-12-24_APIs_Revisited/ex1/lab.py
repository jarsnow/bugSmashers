from flask import Flask, render_template, request, jsonify
import json
from itertools import count

app = Flask(__name__)

# Counter for task IDs
id_counter = count(start=1)

# Load tasks from tasks.json
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    return tasks

# Save tasks to tasks.json
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

# Route to get all tasks
@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    content = request.form['content']
    tasks = load_tasks()
    task = {'id': next(id_counter), 'content': content}
    tasks.append(task)
    save_tasks(tasks)
    return render_template('index.html', tasks=tasks)

# Route to remove a task
@app.route('/remove', methods=['POST'])
def remove_task():
    task_id = int(request.form['task_id'])
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
