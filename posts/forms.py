from wtforms import Form, StringField, TextAreaField

class FormPost(Form):
	title = StringField('Title Post')
	content = TextAreaField('Content')
