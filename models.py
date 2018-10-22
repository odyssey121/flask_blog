from app import db
from datetime import datetime
from sqlalchemy.sql.functions import current_timestamp
import re
from datetime import datetime


def slugify(title):
	pattern = r'[^\w+]'
	half_slug = re.sub(pattern,'_',title)
	time = str(datetime.now().timestamp())
	return half_slug + time[-7:]

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(50))
	subtitle = db.Column(db.String(50))
	author = db.Column(db.String(20))
	date_posted = db.Column(db.DateTime, default = current_timestamp())
	content = db.Column(db.Text)
	slug = db.Column(db.String, unique = True)

	def __init__(self, *args, **kwargs):
		super(Post, self).__init__(*args, **kwargs)
		#self.subtitle = self.content[:20].title() + '...'
		self.subtitle = self.content[:20]
		self.generate_slug()


	def generate_slug(self):
		self.slug = slugify(self.title[:12])
	


	def __repr__(self):
		return 'id = {} ,title = {} , author = {} '.format(
							self.id, self.title, self.author
													   		)
