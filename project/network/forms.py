from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField,FileAllowed

class SshxForm(FlaskForm):
    address = StringField("ipaddress",validators=[DataRequired()])
    port = StringField("port",validators=[DataRequired()])
    username = StringField("username",validators=[DataRequired()])
    command = StringField("command",validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired()])
    submit = SubmitField("Submit")

class ProxyForm(FlaskForm):
    remarks = StringField("remarks",validators=[DataRequired()])
    address = StringField("ipaddress",validators=[DataRequired()])
    port = StringField("port",validators=[DataRequired()])
    username = StringField("username",validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired()])
    submit = SubmitField("Submit")

class TestForm(FlaskForm):
    address = SelectField('代理主机')
    proxyid = StringField('address',validators=[DataRequired()])
    submit = SubmitField('Submit')