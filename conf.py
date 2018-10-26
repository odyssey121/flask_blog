
class Configuration(object):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:////virtualenv/flask_blog/app/base.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'secret'
