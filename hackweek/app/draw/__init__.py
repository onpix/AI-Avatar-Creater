from flask import Blueprint

draw = Blueprint('draw',__name__,static_folder='static',static_url_path='/static')

import app.draw.views