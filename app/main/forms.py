from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,FileField
from wtforms.validators import DataRequired

class BlogForm(FlaskForm):
    blog_pic_path = FileField("Upload Thumbnail", validators=[DataRequired()])
    title = StringField('Blog Title', validators=[DataRequired()])
    category = SelectField(u'Select Blog Category', choices=[('Lifestyle', 'Lifestyle'), ('Travel', 'Travel')], validators=[DataRequired()])
    description = TextAreaField('Blog Description', validators=[DataRequired()])
    submit = SubmitField('ADD POST')