# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import and register blueprints
    from .routes.coffee import coffee_bp
    from .routes.orders import orders_bp

    app.register_blueprint(coffee_bp)
    app.register_blueprint(orders_bp)

    return app
