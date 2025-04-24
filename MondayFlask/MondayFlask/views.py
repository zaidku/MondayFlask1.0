from flask import Blueprint, render_template, request, jsonify
from datetime import datetime
from MondayFlask.model import db, Task

views = Blueprint('views', __name__)

# ===== STATIC PAGES =====

@views.before_request
def log_request_info():
    print(f" Incoming: {request.method} {request.url}")



@views.route('/')
@views.route('/home')
def home():
    return render_template('index.html', title='Home Page', year=datetime.now().year)

@views.route('/contact')
def contact():
    return render_template('contact.html', title='Contact', year=datetime.now().year, message='Your contact page.')

@views.route('/about')
def about():
    return render_template('about.html', title='About', year=datetime.now().year, message='Your application description page.')

# ===== API =====

@views.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@views.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    task = Task(
        title=data.get("title"),
        description=data.get("description"),
        type=data.get("type"),
        priority=data.get("priority"),
        status=data.get("status"),
        assigned_to=data.get("assigned_to"),
        due_date=data.get("due_date")
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({"success": True, "task": task.to_dict()}), 201



@views.route('/api/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"success": True, "message": "Task deleted"})



@views.route('/api/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.json
    for key in ['title', 'description', 'type', 'priority', 'status', 'assigned_to', 'due_date', 'progress']:
        if key in data:
            setattr(task, key, data[key])
    db.session.commit()
    return jsonify({"success": True, "task": task.to_dict()}), 200




@views.route('/ping')
def ping():
    return jsonify({"status": "ok"})



