
class Configuration(object):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:////virtualenv/flask_blog/app/base.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'secret'
	SECURITY_PASSWORD_SALT = 'SALT'
	SECURITY_PASSWORD_HASH = 'sha256_crypt'
