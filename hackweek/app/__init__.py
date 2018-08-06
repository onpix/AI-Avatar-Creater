from flask import Flask
app = Flask(__name__)
# app.debug=True
from app.main import main as main_blueprint
from app.draw import draw as draw_blueprint
from app.crawl import crawl as crawl_blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(draw_blueprint,url_prefix = "/draw")
app.register_blueprint(crawl_blueprint,url_prefix = "/crawl")
