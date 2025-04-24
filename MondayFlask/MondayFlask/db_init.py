from MondayFlask import create_app, db
from MondayFlask.model import Task

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    print("✅ Tables created")

    sample_task = Task(
        title="Sample Task",
        description="Created during db init",
        type="Feature",
        priority="High",
        status="To Do",
        assigned_to="Zaid",
        due_date="2025-04-30"
    )

    db.session.add(sample_task)
    db.session.commit()
    print("✅ Sample task inserted")
