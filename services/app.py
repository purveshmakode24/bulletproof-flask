from flask import Flask
from controller import api
from utility.commons import LOG
from orm.config import Config, db, migrate
import logging

app = Flask(__name__)


app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# from orm.models import Product

logging.basicConfig(
    filename=str(LOG),
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

log = logging.getLogger('app.py')


# main driver function
if __name__ == '__main__':
    db.init_app(app)
    migrate.init_app(app, db)

    # lazily initalized flask-restx
    api.init_app(app)

    # with app.app_context():
    #     db.create_all()

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
