from db.model import db
from parserweb import create_app

from parserweb.parser import return_parsed_data, save_data
db.drop_all(app=create_app())
db.create_all(app=create_app())
app = create_app()
with app.app_context():
    for row in return_parsed_data():
        save_data(row)
