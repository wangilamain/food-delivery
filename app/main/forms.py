from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,ValidationError,SubmitField,SelectField
from wtforms.validators import Required,Email
from ..models import User
from flask_login import current_user

class PitchForm(FlaskForm):

    title = StringField('Title',validators=[Required()])
    content = TextAreaField('Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner')],
                           validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = StringField('Comment', validators=[Required()])
    submit = SubmitField('Post')


class Vote(FlaskForm):
    submit = SelectField('Like')


class UpdateProfile(FlaskForm):
    username = StringField('Enter Username',validators=[Required()])
    email = StringField('Email Address',Email(),validators=[Required()])
    bio = TextAreaField('bio', validators=[Required()])
    submit = SubmitField('Post')

    def validate_email(self,email):
        if email.data != current_user.email:
            if User.query.filter_by(email = email.data).first():
                 raise ValidationError("The Email has already been taken!")
    
    def validate_username(self, username):
        if username.data != current_user.username:
            if User.query.filter_by(username = username.data).first():
                raise ValidationError("The username has already been taken")

