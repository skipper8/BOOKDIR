#This is the main library page
#IMPORTS______________________________________________________________________________
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://morganharper:saphire@localhost:5432/library'
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    IBSN = db.Column(db.String(50))
    tittle = db.Column(db.String(50))
    author = db.Column(db.String(50))
    publisher = db.Column(db.String(50))
    year = db.Column(db.Integer)
    value = db.Column(db.Float)
    cost = db.Column(db.Float)
    
    def __init__(self, IBSN, tittle, author, publisher, year, value, cost):
        self.IBSN = IBSN
        self.tittle = tittle
        self.author = author
        self.publisher = publisher
        self.year = year
        self.value = value
        self.cost = cost

if __name__ == '__main__':
    db.create_all()
