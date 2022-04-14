from db.model import db
from __init__ import create_app

db.create_all(app=create_app())
