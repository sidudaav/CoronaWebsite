from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MapForm(FlaskForm):
    keyword = StringField('Keyword', validators=[DataRequired()])
    time_range1 = StringField('First Time Range', validators=[DataRequired()])
    time_range2 = StringField('Second Time Range', validators=[DataRequired()])
    submit = SubmitField('Get Map')

class DataForm(FlaskForm):
    keyword = StringField('Keyword', validators=[DataRequired()])
    time_range1 = StringField('First Time Range', validators=[DataRequired()])
    time_range2 = StringField('Second Time Range', validators=[DataRequired()])
    submit = SubmitField('Get Data')

class KwPlotForm(FlaskForm):
    keyword1 = StringField('Enter the First Keyword', validators=[DataRequired()])
    keyword2 = StringField('Enter the Second Keyword')
    keyword3 = StringField('Enter the Third Keyword')
    keyword4 = StringField('Enter the Fourth Keyword')
    keyword5 = StringField('Enter the Fifth Keyword')

    location  = StringField("Enter the Location", validators = [DataRequired()])
    time_range = StringField('Time Range', validators=[DataRequired()])
    submit = SubmitField('Get Plot')