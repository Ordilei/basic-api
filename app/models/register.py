from app import db
from app import manager

class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projeto = db.Column(db.String(100))
    ponto = db.Column(db.String(100))
    time = db.Column(db.DateTime)

db.create_all()
manager.create_api(Register, methods=['POST','DELETE','GET'])
