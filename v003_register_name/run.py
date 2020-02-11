from app import create_app, db 
from app.models import Name

app = create_app()

@app.shell_context_processor
def make_shell_context():
	return dict(db=db, Name=Name)

if __name__ == '__main__':
    app.run(debug=True)