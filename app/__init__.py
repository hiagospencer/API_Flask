from flask import Flask
from app.core.config import Config
from app.core.database import db
from app.core.extensions import migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.users.routes import users_bp
    from app.main.routes import main_bp
    
    app.register_blueprint(users_bp)
    app.register_blueprint(main_bp)
    
    return app