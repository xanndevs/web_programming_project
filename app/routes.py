from flask import render_template
from app import app

from app.models import User

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', content="AZAAAAAAAAAAAAAA")



@app.route("/aglaindex")
def aindex():
    users = User.query.all()
    user = users[0]
    return str(user.id) + user.username + user.email