from app import app
from flask import render_template, request, redirect, url_for
from app import mapcode as mc
from app.forms import MapForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('base.html', title = 'Home')

@app.route('/map', methods = ['GET', 'POST'])
def map():
    form  = MapForm()

    if form.validate_on_submit():
        user_keyword = form.keyword.data
        user_time_range = form.time_range.data
        
        mc.get_map(user_keyword, user_time_range)
        image = '/static/MapsHolder/' + str(user_keyword) + 'Map.png'

        return render_template('mapresult.html', title = 'Map Results', image = image)

    return render_template('mapinput.html', title = 'Map Inputs', form = form)


