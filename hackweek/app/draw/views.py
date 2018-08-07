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
    # Add to fix None
    if not imgToTrain:
        return None
    form = request.form
    print(form)
    path = basedir +"/static/train/"
    print(basedir)
    print(path)
    file_path = path +imgToTrain.filename
    imgToTrain.save(file_path)
    in_name = form.get('model')+'.jpg'
    style_weight = int(form.get('times'))
    num_steps = int(form.get('level'))
    #print('[test] path:\n {}\n{}\n{}'.format(in_name, imgToTrain.filename, in_name))
    imageTransfer.main(style_name=in_name, origin_name=imgToTrain.filename, out_name=imgToTrain.filename, num_steps=num_steps, style_weight=style_weight)
    print(file_path)
    return "/draw/static/out/"+imgToTrain.filename
