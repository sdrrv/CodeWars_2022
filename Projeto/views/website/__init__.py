from cgi import test
from flask import Flask
from .views import views
from .auth import auth
from .tester import tester

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "Adoro Nestum"

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(tester, url_prefix="/")

    return app