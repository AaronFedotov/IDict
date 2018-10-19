from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField

class TranslationForm(FlaskForm):
	entry = StringField('Start writing something: ')
	