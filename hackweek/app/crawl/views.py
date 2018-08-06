from . import api_demo1
from . import api_demo2
from . import crawl
from flask import render_template,request    
USER_NUM = 0
# OUT_PATH = '/run/media/why/DATA/why的程序测试/AI_Lab/AI-Avatar-Creater/hackweek/app/crawl/static/out'
OUT_PATH = '/craw/static/out'

@crawl.route('/',methods=['GET'])
def crawl_main():
    return render_template('crawl.html')
@crawl.route('/',methods=['POST'])
def data_load():
    data = request.form
    print(request.form)
    request.form
    # args:
    tune  =10*int(data.get('level'))
    model_num = int(data.get('models'))-1
    img_num = int(data.get('number'))
    mode = int(data.get('situation'))
    global USER_NUM
    out_path=OUT_PATH +'/{}.jpg'.format(USER_NUM)

    print('[test]tune={}\nmodel_num={}\nimg_num={}\nmode={}\nout_path={}'.format(tune, mode
    , img_num, mode, out_path))



    if mode == 6 or mode == 2:
        api_demo1.main(mode=mode, out_path=out_path, tune=tune, model_num=model_num, batch_size=img_num)
    elif mode ==3 or mode ==4:
        api_demo2.main(mode=mode, out_path=out_path, tune=tune, model_num=model_num, batch_size=img_num)
    USER_NUM += 1
#################################################
    return '/crawl/static/out/{}.jpg'.format(USER_NUM-1)




    
