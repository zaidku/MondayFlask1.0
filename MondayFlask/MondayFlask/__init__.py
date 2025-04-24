from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    print(f"📦 Using DB file at: {app.config['SQLALCHEMY_DATABASE_URI']}")


    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['DEBUG'] = True
    app.config['ENV'] = 'development'
    app.config['TESTING'] = True
    app.config['SERVER_NAME'] = 'localhost:5000'
    app.config['APPLICATION_ROOT'] = '/'
    app.config['SESSION_COOKIE_NAME'] = 'session'
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SECURE'] = False
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
    app.config['SESSION_COOKIE_PATH'] = '/'
    app.config['SESSION_COOKIE_DOMAIN'] = None
    app.config['SESSION_COOKIE_EXPIRES'] = None
    app.config['PERMANENT_SESSION_LIFETIME'] = 3600
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['USE_X_SENDFILE'] = False
    app.config['PREFERRED_URL_SCHEME'] = 'http'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
    app.config['JSONIFY_MIMETYPE'] = 'application/json'
    app.config['JSONIFY_USE_JSONLIB'] = False
    app.config['JSONIFY_SORT_KEYS'] = True
    app.config['JSON_SORT_KEYS'] = True
    app.config['JSON_AS_ASCII'] = False


    # Registering the views blueprint
    from MondayFlask.views import views
    app.register_blueprint(views)

    return app
