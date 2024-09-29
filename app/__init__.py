from flask import Flask
from .extensions import db, login_manager  # Импортируйте db и login_manager
from .models.database import User

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)
    login_manager.init_app(app)  # Инициализация LoginManager

    with app.app_context():
        from .routes import main
        app.register_blueprint(main)
        db.create_all()

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
