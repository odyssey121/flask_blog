from flask import Blueprint
from flask import render_template

from flask import request,redirect,url_for,request
from models import Tag,Post
from flask_security import login_required
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



@posts.route('/<slug>/edit', methods = ['POST','GET'])
def post_edit(slug):
	post = Post.query.filter(Post.slug == slug).first()
	if request.method == 'POST':
		form = FormPost(formdata = request.form, obj = post)
		form.populate_obj(obj = post)
		db.session.commit()
		return redirect(url_for('blogs.post_detail', slug = post.slug))

	form = FormPost(obj = post)
	return render_template('posts/post_edit.html', form = form, post = post)


@posts.route('/<slug>')
def post_detail(slug):
	post = Post.query.filter(Post.slug == slug).first()
	tags = post.tags
	return render_template('posts/post_detail.html', post = post, tags = tags)

@posts.route('/tag/<slug>')
def tag_detail(slug):
	page = request.args.get('page')
	if page and page.isdigit():
		page = int(page)
	else:
		page = 1

	tag = Tag.query.filter(Tag.slug == slug).first()
	posts = tag.posts.order_by(Post.date_posted.desc())
	pages = posts.paginate(page = page, per_page = 5)
	return render_template('posts/tag_detail.html', tag = tag, pages = pages)


@posts.route('/create', methods = ['POST','GET'])
@login_required
def create():
	if request.method == 'POST':
		title = request.form.get('title')
		content = request.form.get('content')
		# tag = request.form.get('tag')
		try:
			# tag = Tag.query.filter(Tag.title == tag).first()
			post = Post(title = title, content = content)
			# post.tags.append(tag)
			db.session.add(post)
			db.session.commit()
		except:
			print("db Error")
		else:
			return redirect(url_for('blogs.index'))

	form = FormPost()
	return render_template('posts/create.html', form = form)







