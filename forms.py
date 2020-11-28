from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class PrimeCalc(FlaskForm):
    number = IntegerField("Number", validators=[DataRequired(),NumberRange(max=99999999999999999)])
    submit = SubmitField('Calculate')
