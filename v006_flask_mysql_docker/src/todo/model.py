from src import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        return f'<Todo: {self.title}>'