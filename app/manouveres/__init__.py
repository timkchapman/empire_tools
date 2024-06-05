from flask import Blueprint

bp = Blueprint('manouveres', __name__)

from ..manouveres import routes