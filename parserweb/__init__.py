from flask import Flask, render_template,Blueprint
from db.model import Rsodata
from db.model import db
from parserweb.parser import return_parsed_data

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
    
    @app.route('/')
    def index():
        title = "Информация по агентам"
        rso_data_column_dict = {
            'id': "Порядковый номер",
            'reestr_number': "Номер в реестре",
            'satisfied': "Соответствует ли",
            'excluded': "Является ли агентом",
            'stopped': "Прекращено ли членство",
            'grade': "Степень членства"
            }
        displayed_col = ['id', 'grade', 'stopped']
        agent_list = Rsodata.query.all()
        columns = Rsodata.__table__.columns.keys()
        print(columns)
        #print(agent_list)
        #print("Everything done")
        #print(title, weather, news_list)
        return render_template('info.html', page_title=title,
                               agent_list=agent_list, columns=columns,
                               rso_data_column_dict=rso_data_column_dict,
                               displayed_col=displayed_col)
        # return render_template('debug.html')

  
    # @app.route('/')
    # def index():
    #     title = "Информация по агентам оценки"
    #     person_list = return_parsed_data()
    #     return render_template('index.html', page_title=title, person_list=person_list)
    
    # blueprint = Blueprint('news', __name__)


    
    return app
