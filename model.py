from database import db

class Model(db.Model):

    id            = db.Column(db.Integer, primary_key=True)
    series  = db.Column(db.Text, nullable=False)
    date =  db.Column(db.Text, nullable=False)
    value = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Parameter saved: {self.parameter}"
