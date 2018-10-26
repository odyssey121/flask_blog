from app import app
import view
from posts.blueprint import posts

app.register_blueprint(posts, url_prefix = "/posts")




#===========_CUSTOM__FILTER======================
@app.template_filter('data_format')
def data_format(fd):
	return fd.strftime('%A, %d. %B %Y %H:%M%p')



if __name__ == "__main__":
	app.run()