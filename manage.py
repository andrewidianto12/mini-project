
### Repair code cause of obsulete library flask script and no migrate command in current flask migrate
import os
from flask_migrate import Migrate
from flask_script import Manager

from run import app
from app import db

app.config.from_object("config.Config")

migrate = Migrate(app, db)
manager = Manager(app)

# manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()