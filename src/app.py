from flask import Flask


from blueprints.ads import bp as ads_bp
from blueprints.auth import bp as auth_bp
from blueprints.images import bp as images_bp
from blueprints.users import bp as users_bp
from blueprints.user_ads import bp as user_ads_bp
from database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.register_blueprint(ads_bp, url_prefix='/ads')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(images_bp, url_prefix='/images')
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(user_ads_bp, url_prefix='/users')
    db.init_app(app)
    return app
