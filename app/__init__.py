from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clave-muy-secreta-luego-la-movemos-a-.env'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/tienda.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    from .routes import main as main_bp
    app.register_blueprint(main_bp)

    return app