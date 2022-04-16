from flask import Flask, render_template,Blueprint
from db.model import Rsodata
from db.model import db
from parserweb.parser import return_parsed_data
rso_data_column_dict = {
    'id': "Порядковый номер",
    'reestr_number': "Номер в реестре",
    'satisfied': "Соответствует ли",
    'excluded': "Является ли агентом",
    'stopped': "Прекращено ли членство",
    'grade': "Степень членства",
    'contacts': "Контакты",
    'organization': "Страховые компании",
    'experience': "Стаж",
    'ensurance': "Страховщик",
    'compensation': "Компенсационный фонд",
    'lfm': "ФИО",
    'url': "ссылка",            
    }
displayed_col = ['lfm', 'grade', 'excluded', 'url']

def create_app():
    columns = Rsodata.__table__.columns.keys()
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)    
    @app.route('/')
    def index():
        title = "Информация по агентам"
        active_agents = ['lfm', 'grade', 'exluded', 'url']
        agent_list = Rsodata.query.all()
        # print(columns)
        #print(agent_list)
        #print("Everything done")
        #print(title, weather, news_list)
        return render_template('info.html', page_title=title,
                               agent_list=agent_list, columns=columns,
                               rso_data_column_dict=rso_data_column_dict,
                               displayed_col=displayed_col)
        # return render_template('debug.html')
    @app.route('/active')
    def filtered():
        title = "Информация активным по агентам"
        agent_list = Rsodata.query.filter(Rsodata.grade.in_(['Действительный член РОО'])).all()
        
        # print(columns)
        #print(agent_list)
        #print("Everything done")
        #print(title, weather, news_list)
        return render_template('info.html', page_title=title,
                               agent_list=agent_list, columns=columns,
                               rso_data_column_dict=rso_data_column_dict,
                               displayed_col=displayed_col)
  
    # @app.route('/')
    # def index():
    #     title = "Информация по агентам оценки"
    #     person_list = return_parsed_data()
    #     return render_template('index.html', page_title=title, person_list=person_list)
    
    # blueprint = Blueprint('news', __name__)


    
    return app
