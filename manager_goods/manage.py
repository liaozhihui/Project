from app import create_app,db
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
from app.models import *


app=create_app()

manager=Manager(app)
migreate=Migrate(app,db)
manager.add_command('db',MigrateCommand)



if __name__ == '__main__':
   manager.run()