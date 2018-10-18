from app import app
import view
from posts.blueprint import posts

app.register_blueprint(posts, url_prefix = "/posts")

if __name__ == "__main__":
	app.run()