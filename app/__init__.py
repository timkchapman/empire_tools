from flask import Flask

from config import Config

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	# Initialise Flask extensions here

	# Register blueprints here
	from app.calculator import bp as calculator_bp
	app.register_blueprint(calculator_bp)

	@app.route('/test/')
	def test_page():
		return '<h1>Testing the Flask Application Factory Pattern</h1>'

	return app
