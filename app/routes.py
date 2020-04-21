from app import app
from flask import render_template, request, redirect, url_for
from app import mapcode as mc
from app.forms import *

@app.route('/')
@app.route('/home')
def home():
    return render_template('NormalTemplates/homepage.html', title = 'Home')

@app.route('/map', methods = ['GET', 'POST'])
def map():
    form  = MapForm()

    if form.validate_on_submit():
        user_keyword = form.keyword.data
        user_time_range1 = form.time_range1.data
        user_time_range2 = form.time_range2.data
        
        mc.get_map(user_keyword, user_time_range1, user_time_range2, False)
        image = '/static/MapsHolder/' + 'Map.png'

        return render_template('NormalTemplates/mapresult.html', title = 'Map Results', image = image)

    return render_template('NormalTemplates/mapinput.html', title = 'Map Inputs', form = form)

@app.route('/data', methods  = ['GET', 'POST'])
def data():
    form  = DataForm()

    if form.validate_on_submit():
        user_keyword = form.keyword.data
        user_time_range1 = form.time_range1.data
        user_time_range2 = form.time_range2.data

        df  = mc.get_data(user_keyword, user_time_range1, user_time_range2, False)

        return render_template('NormalTemplates/dataresult.html',  tables=[df.to_html(classes='data', index = False)],
         title = 'Keyword Results', titles=df.columns.values, keyword = user_keyword)


    return render_template('NormalTemplates/datainput.html', title = "Keyword Inputs", form = form)

@app.route('/kwplot', methods = ['GET', 'POST'])
def kwplot():
    form = KwPlotForm()
    if form.validate_on_submit():
        user_keyword1 = form.keyword1.data
        user_keyword2 = form.keyword2.data
        user_keyword3 = form.keyword3.data
        user_keyword4 = form.keyword4.data
        user_keyword5 = form.keyword5.data

        kw_list_holder = [user_keyword1, user_keyword2, user_keyword3, user_keyword4, user_keyword5]
        kw_list = []

        for ele in kw_list_holder:
            if ele != '':
                kw_list.append(ele)
        
        time_range = form.time_range.data
        location = form.location.data
        mc.kw_plot(time_range, kw_list, location, False)

        image = '/static/MapsHolder/ComparisonPlot.png'

        return render_template('NormalTemplates/kwplotresult.html', title = 'Keywords Plot', image = image)

    return render_template('NormalTemplates/kwplotinput.html', title = 'Keywords Plot', form = form)

@app.route('/youtube-home', methods = ['GET', 'POST'])
def youtube_home():
    return render_template('YoutubeTemplates/youtube_homepage.html', title = 'Youtube Home')

@app.route('/youtube-map', methods = ['GET', 'POST'])
def youtube_map():
    form  = MapForm()

    if form.validate_on_submit():
        user_keyword = form.keyword.data
        user_time_range1 = form.time_range1.data
        user_time_range2 = form.time_range2.data
        
        mc.get_map(user_keyword, user_time_range1, user_time_range2, True)
        image = '/static/MapsHolder/' + 'Map.png'

        return render_template('YoutubeTemplates/youtube_mapresult.html', title = 'Map Results', image = image)

    return render_template('YoutubeTemplates/youtube_mapinput.html', title = 'Map Inputs', form = form)

@app.route('/youtube-data', methods = ['GET', 'POST'])
def youtube_data():
    form  = DataForm()

    if form.validate_on_submit():
        user_keyword = form.keyword.data
        user_time_range1 = form.time_range1.data
        user_time_range2 = form.time_range2.data

        df  = mc.get_data(user_keyword, user_time_range1, user_time_range2, True)

        return render_template('YoutubeTemplates/youtube_dataresult.html',  tables=[df.to_html(classes='data', index = False)],
         title = 'Keyword Results', titles=df.columns.values, keyword = user_keyword)


    return render_template('YoutubeTemplates/youtube_datainput.html', title = "Keyword Inputs", form = form)

@app.route('/youtube-kwplot', methods = ['GET', 'POST'])
def youtube_kwplot():
    form = KwPlotForm()
    if form.validate_on_submit():
        user_keyword1 = form.keyword1.data
        user_keyword2 = form.keyword2.data
        user_keyword3 = form.keyword3.data
        user_keyword4 = form.keyword4.data
        user_keyword5 = form.keyword5.data

        kw_list_holder = [user_keyword1, user_keyword2, user_keyword3, user_keyword4, user_keyword5]
        kw_list = []

        for ele in kw_list_holder:
            if ele != '':
                kw_list.append(ele)
        
        time_range = form.time_range.data
        location = form.location.data
        mc.kw_plot(time_range, kw_list, location, True)

        image = '/static/MapsHolder/ComparisonPlot.png'

        return render_template('YoutubeTemplates/youtube_kwplotresult.html', title = 'Keywords Plot', image = image)

    return render_template('YoutubeTemplates/youtube_kwplotinput.html', title = 'Keywords Plot', form = form)