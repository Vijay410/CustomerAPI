from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    app.config['JWT_SECRET_KEY'] = 'acgft4rer-1ret4DTE3-GFTERc'
    db.init_app(app)
    jwt.init_app(app)
    migrate = Migrate(app, db)

    from app.views.customer_view import customer_view
    from app.auth.user_auth import auth_bp

    app.register_blueprint(customer_view)
    app.register_blueprint(auth_bp)

    return app