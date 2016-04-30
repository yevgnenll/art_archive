from archive import db


class Artist(db.Model):

    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True)
    birth_year = db.Column(db.Integer)
    death_year = db.Column(db.Integer)
    country = db.Column(db.String(45))
    genre = db.Column(db.String(45))

    def __repr__(self):
        return '<id:{id} artist {name}>'.format(
            id=self.id,
            name=self.name,
        )

    def data_to_dict(self):

        result = {
            'id': self.id,
            'name': self.name,
            'birth_year': self.birth_year,
            'death_year': self.death_year,
            'genre': self.genre,
        }
        return result
