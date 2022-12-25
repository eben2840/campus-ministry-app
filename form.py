from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Regexp








class Form(FlaskForm):
    name = StringField('name')
    number = StringField('number')
    comment = StringField('comment')
    submit = SubmitField('submit')
    
