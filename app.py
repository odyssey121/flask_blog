from flask import Flask
from conf import Configuration
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
#from models import *


