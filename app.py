from flask import Flask
from conf import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import Security,SQLAlchemyUserDatastore

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
from models import *
migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
#============SECURITY=====SECURITY==========
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

#=========ADMIN=========VIEWS=============
admin = Admin(app, name = "Custom-admin")
admin.add_view(ModelView(Post,db.session))
admin.add_view(ModelView(Tag,db.session))
admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(Role,db.session))

