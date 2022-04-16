from db.model import db
from parserweb import create_app

db.create_all(app=create_app())
