from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

"""
class Ensurance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ensurance_org=db.Column(db.String, nullable=True)
"""
    
class Rsodata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reestr_number = db.Column(db.Text)
    satisfied = db.Column(db.String)
    excluded = db.Column(db.Text, nullable=True)
    stopped = db.Column(db.Text, nullable=True)
    grade = db.Column(db.String, nullable=True)
    lfm = db.Column(db.String, nullable=True)
    compensation = db.Column(db.String, nullable=True)
    experience = db.Column(db.String, nullable=True)
    contacts = db.Column(db.Text, nullable=True)
    url = db.Column(db.String, unique=True, nullable=True)
    ensurance=db.Column(db.String, nullable=True)
    def __repr__(self):
        return '<Person info {} {} {} {}>'.format(self.reestr_number, self.satisfied ,self.excluded ,self.url)
        
"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #firstname = db.Column(db.String, nullable=True)
    #lastname = db.Column(db.String, nullable=True)
    #middlename = db.Column(db.String, nullable=True)
    lfm = db.Column(db.String, nullable=True)
    compensation = db.Column(db.String, nullabale=True)
    experience = db.Column(db.String, nullabale=True)
    contacts = db.Column(db.Text, nullable=True)
    #ensurance_id = db.Column(db.Integer, unique=True)
    #rso_id = db.Column(db.Boolean, nullabale=True)  
    url = db.Column(db.String, unique=True, nullable=True)
"""
    
