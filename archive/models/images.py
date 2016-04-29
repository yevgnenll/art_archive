from archive import db

from archive.models import Artist


class Image(db.Model):

    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    year = db.Column(db.Integer)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<id:{id} title: {title}>'.format(
            id=self.id,
            title=self.title,
        )
