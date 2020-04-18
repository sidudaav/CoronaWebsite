from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MapForm(FlaskForm):
    keyword = StringField('Keyword', validators=[DataRequired()])
    time_range = StringField('Time Range', validators=[DataRequired()])
    submit = SubmitField('Get Map')