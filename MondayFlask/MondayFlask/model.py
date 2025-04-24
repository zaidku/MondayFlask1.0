



from MondayFlask import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    type = db.Column(db.String(50))
    priority = db.Column(db.String(50))
    status = db.Column(db.String(50))
    assigned_to = db.Column(db.String(100))
    due_date = db.Column(db.String(50))  # You can use Date type if needed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "type": self.type,
            "priority": self.priority,
            "status": self.status,
            "assigned_to": self.assigned_to,
            "due_date": self.due_date
        }