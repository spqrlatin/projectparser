from parserweb import create_app
from parserweb.parser import return_parsed_data, save_data
app = create_app()
with app.app_context():
    for row in return_parsed_data():
        save_data(row)
