from flask import render_template, request, Flask, flash, redirect, url_for, send_from_directory
from app import app
import os
from werkzeug.utils import secure_filename

from app.models import Show
from app.models import Episode
from app import db

from datetime import datetime
import sys
#app.config['UPLOAD_FOLDER'] = '/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['ALLOWED_VIDEO_EXTENSIONS'] = {'mp4', 'mkv', 'hvec', 'avi', 'webm', 'mov'}

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
def allowed_video(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_VIDEO_EXTENSIONS']


@app.route('/')
@app.route('/index')
def index():
    shows = Show.query.all()
    shows_dict = {show.id: show.title for show in shows}
    all_dict = {show.id: [show.title, show.show_thumbnail, show.description] for show in shows}

    right_panel_html = render_template('content/right_panel_list.html', show_data=shows)
    main_page = render_template('content/index.html', content=all_dict)
    return render_template('main_template.html', title='Homepage', autofill_data=shows_dict, content=main_page, right_panel=right_panel_html)


@app.route("/show/", methods=["GET", "POST"])
@app.route("/show/<show_id>", methods=["GET", "POST"])
def show_page(show_id):
    ##Autofill data
    shows = Show.query.all()
    shows_dict = {show.id: show.title for show in shows}
    
    ##Current show
    show_data = db.session.query(Show).filter(Show.id == show_id).first()
    
    ##Episodes list
    episode_data = db.session.query(Episode).filter(Episode.show_id == show_id)

    right_panel_html = render_template('content/right_panel_list.html', show_data=shows)
    main_html = render_template('content/show_info.html', show_data=show_data, episode_data=episode_data)
    return render_template('main_template.html', title='Homepage', autofill_data=shows_dict, content=main_html, right_panel=right_panel_html)


@app.route("/watch/", methods=["GET", "POST"])
@app.route("/watch/<episode_id>", methods=["GET", "POST"])
def episode_page(episode_id):
    ##Autofill data
    shows = Show.query.all()
    shows_dict = {show.id: show.title for show in shows}
    
    ##Episodes list
    current_episode = db.session.query(Episode).filter(Episode.id == episode_id).first()
    current_show_id = db.session.query(Show).filter(Show.id == current_episode.show_id).first().id

    episode_data = db.session.query(Episode).filter(Episode.show_id == current_show_id)
    
    right_panel_html = render_template('content/right_panel_list.html', episode_data=episode_data)
    main_html = render_template('content/episode_info.html', current_episode=current_episode, episode_data=episode_data)
    return render_template('main_template.html', title='Homepage', autofill_data=shows_dict, content=main_html, right_panel=right_panel_html)































@app.route("/add-show", methods=["GET", "POST"])
def add_show():
    page_info = ""
    if request.method == 'POST':

        form_data = request.form
        files = request.files.getlist("thumbnail")

        file = files[0]
        new_filename = ""
        if file and allowed_file(file.filename):
            
            current_date = datetime.now()
            formatted_date = current_date.strftime("%H_%M_%S")

            new_filename = form_data.get("title")+"_Thumbnail_"+formatted_date+"."+file.filename.split(".")[-1]
            new_filename = new_filename.replace(" ","_")

            filepath = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
            file.save(filepath)


        # Commit the values to the DB.
        new_show = Show(
            title = form_data.get("title"),
            description = form_data.get("description"),
            show_thumbnail = new_filename
        )
        db.session.add(new_show)
        db.session.commit()
        page_info = "Show added to the database"


    ##Autofill data
    shows = Show.query.all()
    shows_dict = {show.id: show.title for show in shows}

    right_panel_html = render_template('content/right_panel_list.html', show_data=shows)
    main_html = render_template('add-show.html', page_info=page_info)
    return render_template('main_template.html', title='Homepage', autofill_data=shows_dict, content=main_html, right_panel=right_panel_html)

@app.route('/uploads/')
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)







@app.route("/add-episode", methods=["GET", "POST"])
def add_episode():
    page_info = ""

    ##Autofill data
    shows = Show.query.all()
    shows_dict = {show.id: show.title for show in shows}
    
    if request.method == 'POST':
        form_data = request.form
        files = request.files.getlist("video")

        file = files[0]
        new_filename = ""
        if file and allowed_video(file.filename):
            current_date = datetime.now()
            formatted_date = current_date.strftime("%H_%M_%S")

            new_filename = shows_dict.get(int(form_data.get('show-id')))+"_"+form_data.get('title')+"_Video_"+formatted_date+"."+file.filename.split(".")[-1]
            new_filename = new_filename.replace(" ","_")

            filepath = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
            file.save(filepath)

        # Commit the values to the DB.
        new_episode = Episode(
            title = form_data.get("title"),
            description = form_data.get("description"),
            episode_video = new_filename,
            show_id = form_data.get('show-id')
        )
        db.session.add(new_episode)
        db.session.commit()

        page_info = "Episode added to the database"


    right_panel_html = render_template('content/right_panel_list.html', show_data=shows)
    main_html = render_template('add-episode.html', autofill_data=shows_dict, page_info=page_info)
    return render_template('main_template.html', title='Homepage', autofill_data=shows_dict, content=main_html, right_panel=right_panel_html)

