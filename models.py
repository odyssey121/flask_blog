from app import db
from datetime import datetime
from sqlalchemy.sql.functions import current_timestamp
import re
from datetime import datetime
from flask_security import UserMixin,RoleMixin

def slugify(title,is_tag = False):
	pattern = r'[^\w+]'
	half_slug = re.sub(pattern,'_',title)
	if is_tag:
		return half_slug
	else:
		time = str(datetime.now().timestamp())
		return half_slug + time[-7:]

class Tag(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(50), unique = True)
	slug = db.Column(db.String(50), unique = True)

	def __init__ (self, *args, **kwargs):
		super(Tag, self).__init__(*args, **kwargs)
		self.slug = slugify(self.title,is_tag = True)	

	def __repr__(self):
		return 'tag id = {}, tag title = {}'.format(self.id, self.title)

post_tags = db.Table('post_tags',
	db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
	db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')))

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(50))
	subtitle = db.Column(db.String(50))
	author = db.Column(db.String(20))
	date_posted = db.Column(db.DateTime, default = datetime.now())
	content = db.Column(db.Text)
	slug = db.Column(db.String, unique = True)

	def __init__(self, *args, **kwargs):
		super(Post, self).__init__(*args, **kwargs)
		#self.subtitle = self.content[:20].title() + '...'
		self.subtitle = self.content[:20]
		self.generate_slug()

	tags = db.relationship('Tag', secondary = post_tags, backref = db.backref('posts', lazy = 'dynamic'))

	def generate_slug(self):
		self.slug = slugify(self.title[:12])
	
	def __repr__(self):
		return 'id = {} ,title = {} , author = {} '.format(self.id, self.title, self.author)

#=========USER_PERSON===========USER_PERSON======================

roles_users = db.Table('roles_users',
	db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
	db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class User(db.Model,UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), unique=True)
	email = db.Column(db.String(120), unique = True)
	password = db.Column(db.String(255))
	active = db.Column(db.Boolean())
	roles = db.relationship('Role', secondary = roles_users, backref = db.backref('users', lazy = 'dynamic'))

class Role(db.Model,RoleMixin):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), unique=True)
	description = db.Column(db.Text)
