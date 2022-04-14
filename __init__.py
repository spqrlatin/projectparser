from flask import Flask, render_template

from db.model import db
from parser import return_parsed_data

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
    @app.route('/')
    def index():
        title = "Информация по агентам оценки"
        person_list = return_parsed_data()
        return render_template('index.html', page_title=title, person_list=person_list)
    
    return app
