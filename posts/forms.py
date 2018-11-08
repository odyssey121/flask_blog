from wtforms import Form, StringField, TextAreaField, SelectField
from models import Tag

class FormPost(Form):
	title = StringField('Title Post')
	content = TextAreaField('Content')
	# tag = StringField('Tag')
	# tags = SelectField('Tags', choices = [tag.title for  tag in Tag.query.all()])

