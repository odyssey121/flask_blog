from flask import Blueprint
from flask import render_template

from flask import request,redirect,url_for,request
from models import Post
from app import db
from .forms import FormPost



posts = Blueprint('blogs',__name__, template_folder = 'templates/')

@posts.route('/')
def index():
	query = request.args.get('query')
	page = request.args.get('page')
	if page and page.isdigit():
		page = int(page)
	else:
		page = 1

	if query:
		posts = Post.query.filter(Post.title.contains(query) | Post.content.contains(query))
	else:
		posts = Post.query.order_by(Post.date_posted.desc())
	
	pages = posts.paginate(page = page, per_page = 10)
	return render_template('posts/index.html', pages = pages)

@posts.route('/<slug>')
def post_detail(slug):
	post = Post.query.filter(Post.slug == slug).first()
	return render_template('posts/post_detail.html', post = post)


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







