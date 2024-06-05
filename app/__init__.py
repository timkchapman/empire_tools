from flask import Flask
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask import render_template

db = SQLAlchemy()

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	# Initialise Flask extensions here
	csrf = CSRFProtect()
	csrf.init_app(app)
	db.init_app(app)

	# Register blueprints here
	from app.calculator import bp as calculator_bp
	app.register_blueprint(calculator_bp)

	from app.manouveres import bp as manouveres_bp
	app.register_blueprint(manouveres_bp)

	@app.route('/')
	def index():
		return render_template('index.html')

	return app
