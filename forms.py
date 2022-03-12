from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

from wtforms.validators import DataRequired, ValidationError,Email,Length,EqualTo
from models import User

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=15)])
    submit = SubmitField("login")
    
    
class RegistrationForm(FlaskForm):
        email = StringField("Email", validators=[DataRequired(), Email()])
        password = StringField("Password", validators=[DataRequired(), Length(min=6,max=15)])
        password_confirm = StringField("Confirm Password", validators=[DataRequired(), Length(min=6,max=15), EqualTo('password')])
        first_name = StringField("First Name", validators=[DataRequired(),Length(min=5,max=25)])
        last_name = StringField("Last Name", validators=[DataRequired(),Length(min=5,max=25)])
        submit = SubmitField("Register Now!")
        
        def validate_email(self,email):
            user = User.objects(email= email.data).first()
            if user:
                raise ValidationError("Email is already in use. pick another one.")
            