from app import db
from datetime import datetime

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(50))
	subtitle = db.Column(db.String(50))
	author = db.Column(db.String(20))
	date_posted = db.Column(db.DateTime(datetime.now()))
	content = db.Column(db.Text)

	def __init__(self, *args, **kwargs):
		super(Post, self).__init__(*args, **kwargs)


	def __repr__(self):
		return 'id = {} ,title = {} , author = {} '.format(
							self.id, self.title, self.author
													   		)
