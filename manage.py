from dotenv import load_dotenv
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
import os


# refers to application_top
APP_ROOT = os.path.join(os.path.dirname(__file__), '.')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

config_name = os.environ.get('APP_SETTINGS')
app = create_app(config_name)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    app.run(debug=True)
