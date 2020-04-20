from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MapForm(FlaskForm):
    keyword = StringField('Keyword', validators=[DataRequired()])
    time_range1 = StringField('First Time Range', validators=[DataRequired()])
    time_range2 = StringField('Second Time Range', validators=[DataRequired()])
    submit = SubmitField('Get Map')

class kwForm(FlaskForm):
    keyword = StringField('Keyword', validators=[DataRequired()])
    time_range1 = StringField('First Time Range', validators=[DataRequired()])
    time_range2 = StringField('Second Time Range', validators=[DataRequired()])
    submit = SubmitField('Get Data')