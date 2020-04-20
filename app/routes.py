from app import app
from flask import render_template, request, redirect, url_for
from app import mapcode as mc
from app.forms import MapForm
from app.forms import kwForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html', title = 'Home')

@app.route('/map', methods = ['GET', 'POST'])
def map():
    form  = MapForm()

    if form.validate_on_submit():
        user_keyword = form.keyword.data
        user_time_range1 = form.time_range1.data
        user_time_range2 = form.time_range2.data
        
        mc.get_map(user_keyword, user_time_range1, user_time_range2)
        image = '/static/MapsHolder/' + str(user_keyword) + 'Map.png'

        return render_template('mapresult.html', title = 'Map Results', image = image)

    return render_template('mapinput.html', title = 'Map Inputs', form = form)

@app.route('/data', methods  = ['GET', 'POST'])
def data():
    form  = kwForm()

    if form.validate_on_submit():
        user_keyword = form.keyword.data
        user_time_range1 = form.time_range1.data
        user_time_range2 = form.time_range2.data

        df  = mc.get_data(user_keyword, user_time_range1, user_time_range2)
        return render_template('kwresult.html',  tables=[df.to_html(classes='data', index = False)],
         title = 'Keyword Results', titles=df.columns.values, keyword = user_keyword)


    return render_template('kwinput.html', title = "Keyword Inputs", form = form)


