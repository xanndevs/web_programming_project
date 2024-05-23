from app import db

#class Show(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    videoId = db.Column(db.String(16), )
#    episodeNumber = db.Column(db.String(64), index=True, unique=True)
#    title = db.Column(db.String(64), index=True, unique=True)
#    description = db.Column(db.String(512))
#    date = db.Column(db.DateTime(128))
#
#    def __repr__(self):
#        return '<Title {}>'.format(self.title)

class Show(db.Model):
    __tablename__ = 'show'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    show_thumbnail= db.Column(db.String, nullable=True)
    episode = db.relationship('Episode', backref='show', lazy=True)

class Episode(db.Model):
    __tablename__ = 'episode'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    episode_video = db.Column(db.String, nullable=False)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)
