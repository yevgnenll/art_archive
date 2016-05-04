from archive import db

from flask import abort


class Artist(db.Model):

    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True)
    birth_year = db.Column(
        db.Integer,
        nullable=True,
    )
    death_year = db.Column(
        db.Integer,
        nullable=True,
    )
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

    def detail_to_dict(self, datas):

        masterpiece = []
        for data in datas:
            title = {}
            title['title'] = data.title
            masterpiece.append(title)

        result = self.data_to_dict()
        result['masterpiece'] = masterpiece

        return result

    def data_get_as_dict(self, params):

        birth = params.get('birth_year')
        death = params.get('death_year')

        try:
            birth = int(birth)
            death = int(death)
        except:
            abort(400)

        self.name = params['name']
        self.birth_year = birth
        self.death_year = death
        self.country = params['country']
        self.genre = params['genre']

        return self
