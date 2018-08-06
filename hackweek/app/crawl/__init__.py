from flask import Blueprint

crawl = Blueprint('crawl',__name__,static_folder='static',static_url_path='/static')

import app.crawl.views


