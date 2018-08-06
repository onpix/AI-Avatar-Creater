from . import api_demo1
from . import crawl
from flask import render_template,request    
USER_NUM = 0

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
    out_path='./static/out/{}.jpg'.format(USER_NUM)
    if mode == 6 or mode == 2:
        api_demo1.main(mode=mode, out_path=out_path, tune=tune, model_num=model_num, img_num=img_num)
    USER_NUM += 1
#################################################

    return data;




    
