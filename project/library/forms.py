from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField
from wtforms.validators import DataRequired

class MailForm(FlaskForm):
    usermail = StringField('email',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    serveraddr = StringField('server',validators=[DataRequired()])
    port = StringField('port',validators=[DataRequired()])
    submit = SubmitField('submit')
