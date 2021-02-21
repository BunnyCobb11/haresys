from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from project.models import User

class LoginForm(FlaskForm):
    email = StringField('邮箱：',validators=[DataRequired(),Email()])
    password = PasswordField('密码：',validators=[DataRequired()])
    submit = SubmitField('登录')

class RegistrationForm(FlaskForm):
    email = StringField('邮箱',validators=[DataRequired(),Email()])
    username = StringField('用户名',validators=[DataRequired()])
    password = PasswordField('密码：',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match!')])
    pass_confirm = PasswordField('确认密码',validators=[DataRequired()])
    submit = SubmitField('注册')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been registered already!')


class UpdateUserForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('UserName',validators=[DataRequired()])
    picture = FileField('更新头像',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been registered already!')
