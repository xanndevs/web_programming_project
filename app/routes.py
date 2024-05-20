from flask import render_template, request, Flask, flash, redirect, url_for, send_from_directory
from app import app
import os
from werkzeug.utils import secure_filename

from app.models import Show
from app.models import Episode
from app import db




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
    return render_template('index.html', title='Home', content="AZAAAAAAAAAAAAAA", videoID="jvid")


@app.route("/aglaindex")
def aindex():
    users = Show.query.all()
    user = users[0]
    return str(user.id) + "<br>" + user.title + "<br>" + user.description


@app.route("/add-show", methods=["GET", "POST"])
def add_show():
    if request.method == 'POST':
        form_data = request.form
        files = request.files.getlist("thumbnail")

        saved_files = []
        file = files[0]
        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            saved_files.append(filename)


        # Commit the values to the DB.
        new_show = Show(
            show_name = form_data.get("title"),
            show_description = form_data.get("description"),
            show_thumbnail = file.filename
        )
        db.session.add(new_show)
        db.session.commit()

        # Generate HTML to display form data and images
        result = f"<h1>Received Form Data:</h1><ul>"
        for key, value in form_data.items():
            result += f"<li>{key}: {value}</li>"
        result += "</ul>"

        if saved_files:
            result += "<h2>Uploaded Images:</h2>"
            for filename in saved_files:
                img_url = url_for('uploaded_file', filename=filename)
                result += f'<div><img src="{img_url}" alt="{filename}" style="max-width:200px;"><p>{filename}</p></div>'
        
        return result
    else:
        return render_template('add-show.html', title='Home', content="AZAAAAAAAAAAAAAA", videoID="jvid")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)







@app.route("/add-episode", methods=["GET", "POST"])
def add_episode():
    if request.method == 'POST':
        form_data = request.form
        files = request.files.getlist("video")

        saved_files = []
        file = files[0]
        if file and allowed_video(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            saved_files.append(filename)


        # Commit the values to the DB.
        new_show = Episode(
            show_name = form_data.get("title"),
            show_description = form_data.get("description"),
            show_thumbnail = file.filename
        )
        db.session.add(new_show)
        db.session.commit()

        # Generate HTML to display form data and images
        result = f"<h1>Received Form Data:</h1><ul>"
        for key, value in form_data.items():
            result += f"<li>{key}: {value}</li>"
        result += "</ul>"

        if saved_files:
            result += "<h2>Uploaded Images:</h2>"
            for filename in saved_files:
                vid_url = url_for('uploaded_file', filename=filename)
                result += f'<div><video alt="{filename}" style="max-width:200px;"><source src="{vid_url}" type="video/{filename.split(".")[-1]}"></video><p>{filename}</p></div>'
        
        return result
    else:
        shows = Show.query.all()
        shows_dict = {show.id: show.show_name for show in shows}
        return render_template('add-episode.html', title='Add Episode', autofill_data=shows_dict)




