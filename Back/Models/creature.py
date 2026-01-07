from Back.database import db

class Creature(db.Model):
    __tablename__ = "creature"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    max_HP = db.Column(db.Integer, nullable=False)
    atm_HP = db.Column(db.Integer, nullable=False, default=0)
    additional_info = db.Column(db.Text, nullable=True)