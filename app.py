from flask import Flask
from conf import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import Security,SQLAlchemyUserDatastore,current_user
from flask_admin import AdminIndexView
from flask import redirect,url_for,request

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
from models import *
migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

#=========ADMIN=========VIEWS=============
class AbstractModel(ModelView):
	def is_accessible(self):
		return current_user.has_role("admin")
	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('login', next = request.url))
class MyView(AbstractModel):
	pass
class HomeAdminView(AdminIndexView):
	def is_accessible(self):
		return current_user.has_role("admin")
	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('login', next = request.url))
#==========================================	
admin = Admin(app, "Custom-admin", url = "/",
	        index_view = HomeAdminView(name = "Custom-admin"))
admin.add_view(MyView(Post,db.session))
admin.add_view(MyView(Tag,db.session))
admin.add_view(MyView(User,db.session))
admin.add_view(MyView(Role,db.session))

#============SECURITY=====SECURITY==========
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

