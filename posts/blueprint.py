from flask import Blueprint
from flask import render_template

from flask import request,redirect,url_for
from models import Post
from app import db
from .forms import FormPost



posts = Blueprint('blogs',__name__, template_folder = 'templates/')

@posts.route('/')
def index():
	posts = Post.query.all()
	return render_template('posts/index.html', posts = posts)

@posts.route('/create', methods = ['POST','GET'])
def create():
	if request.method == 'POST':
		title = request.form.get('title')
		content = request.form.get('content')
		try:
			post = Post(title = title, content = content)
			db.session.add(post)
			db.session.commit()
		except:
			print("db Error")
		else:
			return redirect(url_for('blogs.index'))

	form = FormPost()
	return render_template('posts/create.html', form = form)







