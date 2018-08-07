import os
from . import api_demo1
from . import api_demo2
from . import crawl
from flask import render_template,request    
import hashlib

USER_NUM = 0
file_list = []

# OUT_PATH = '/run/media/why/DATA/why的程序测试/AI_Lab/AI-Avatar-Creater/hackweek/app/crawl/static/out'
basedir = os.path.dirname(__file__)
OUT_PATH = basedir + '/static/out'
@crawl.route('/',methods=['GET'])
def crawl_main():
    return render_template('crawl.html')

def del_pic(files):

    if len(files) > 100:
        for a in files:
            os.remove(a)

@crawl.route('/',methods=['POST'])
def data_load():
    data = request.form
    print(request.form)
    request.form
    # args:
    tune = 100-10*int(data.get('level'))
    model_num = int(data.get('models'))-1
    img_num = int(data.get('number'))
    mode = int(data.get('situation'))

    del_pic(file_list)
    # Hash
    md5 = hashlib.md5()
    global USER_NUM
    md5.update(bytes(str(USER_NUM), encoding="ascii"))
    tmp_name = md5.hexdigest()

    out_path=OUT_PATH +'/{}.jpg'.format(tmp_name)

    print('[test]tune={}\nmodel_num={}\nimg_num={}\nmode={}\nout_path={}'.format(tune, model_num
    , img_num, mode, out_path))



    if mode == 6 or mode == 2:
        api_demo1.main(mode=mode, out_path=out_path, tune=tune, model_num=model_num, batch_size=img_num)
    elif mode ==3 or mode ==4:
        api_demo2.main(mode=mode, out_path=out_path, tune=tune, model_num=model_num, batch_size=img_num)
    USER_NUM += 1

    file_list.append(out_path)
#################################################
    return '/crawl/static/out/{}.jpg'.format(tmp_name)







    
