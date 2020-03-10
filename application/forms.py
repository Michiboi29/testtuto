from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Nom du tulateur', validators=[DataRequired()])
    password = PasswordField('Mot de passe passe', validators=[DataRequired()])
    remember_me = BooleanField('Se souvenir de ma pauvre âme')
    submit = SubmitField("S'inscrire")