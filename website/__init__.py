#  initialization of flask app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import login_manager



#  create flask app 
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "sowemeetagain"
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    return app 