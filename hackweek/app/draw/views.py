from . import draw
from flask import render_template,request
import os
from . import imageTransfer
basedir = os.path.abspath(os.path.dirname(__file__))
@draw.route('/',methods=['GET'])
def drawl_main():
    return render_template('draw.html')
@draw.route('/',methods=["POST"])
def proccess_Data():
    files = request.files
    imgToTrain = files.get('file')
    form = request.form
    print(form)
    path = basedir +"/static/train/"
    print(basedir)
    print(path)
    file_path = path +imgToTrain.filename
    imgToTrain.save(file_path)
    in_name = form.get('model')+'.jpg'
    print('[test] path:\n {}\n{}\n{}'.format(in_name, imgToTrain.filename, in_name))
    imageTransfer.main(style_name=in_name, origin_name=imgToTrain.filename, out_name=in_name, num_steps=1, style_weight=1e5)
    print(file_path)
    return "/static/train/out/"+imgToTrain.filename