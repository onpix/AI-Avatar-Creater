from . import main
from flask import render_template
@main.route('/')
def main_html():
    return render_template('index.html')
