from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,FileField,EmailField
from wtforms.validators import DataRequired, Email

class BlogForm(FlaskForm):
    blog_pic_path = FileField("Upload Thumbnail", validators=[DataRequired()])
    title = StringField('Blog Title', validators=[DataRequired()])
    category = SelectField(u'Select Blog Category', choices=[('Lifestyle', 'Lifestyle'), ('Travel', 'Travel')], validators=[DataRequired()])
    description = TextAreaField('Blog Description', validators=[DataRequired()])
    submit = SubmitField('ADD POST')

class CommentForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired()])
    comment = TextAreaField('Comment*', validators=[DataRequired()])
    submit = SubmitField('POST COMMENT')

class SubscribeForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    email = EmailField('Enter Email to Subscribe', validators=[Email(), DataRequired()])
    submit = SubmitField('SUBSCRIBE')