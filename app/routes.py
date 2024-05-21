from flask import render_template, request, Flask, flash, redirect, url_for, send_from_directory
from app import app
import os
from werkzeug.utils import secure_filename

from app.models import Show
from app.models import Episode
from app import db

from datetime import datetime



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
    shows_dict = {show.id: show.show_name for show in shows}
    return render_template('main_template.html', title='Homepage', autofill_data=shows_dict, content="THERE WILL BE CONTENT")



@app.route("/add-show", methods=["GET", "POST"])
def add_show():
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
            show_name = form_data.get("title"),
            show_description = form_data.get("description"),
            show_thumbnail = new_filename
        )
        db.session.add(new_show)
        db.session.commit()

  
        return "Show have been successfully added!"
    else:
        return render_template('add-show.html', title='Home', content="AZAAAAAAAAAAAAAA", videoID="jvid")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)







@app.route("/add-episode", methods=["GET", "POST"])
def add_episode():
    if request.method == 'POST':
        shows = Show.query.all()
        shows_dict = {show.id: show.show_name for show in shows}

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

        return "Episode have been successfully uploaded!"
    else:
        shows = Show.query.all()
        shows_dict = {show.id: show.show_name for show in shows}
        return render_template('add-episode.html', title='Add Episode', autofill_data=shows_dict)




@app.route("/show", methods=["GET", "POST"])
def show_page():
    shows = Show.query.all()
    shows_dict = {show.id: show.show_name for show in shows}
    main_html = render_template('add-show.html', title='Home', content="AZAAAAAAAAAAAAAA", videoID="jvid")
    return render_template('main_template.html', title='Homepage', autofill_data=shows_dict, content=main_html)