import os, locale

from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt

# db = SQLAlchemy()
# bcrypt = Bcrypt()

# DB_SERVER   = "localhost"
# DB_PORT     = "3306"
# DB_USERNAME = "root"
# DB_PASSWORD = ""
# DB_NAME     = "practice_flask"

# UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

# # Ensure the upload folder exists
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)
    
def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'My Secret Key'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}'
    # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    # db.init_app(app)
    # bcrypt.init_app(app)
    
    from application.apis.authentication import authentication
    
    app.register_blueprint(authentication)
    
    return app
