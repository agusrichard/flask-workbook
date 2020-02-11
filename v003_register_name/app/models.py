from . import db

class Name(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))

	def __repr__(self):
		return '{}'.format(self.name)