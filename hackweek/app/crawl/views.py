from api_demo1 import main as main1
from . import crawl
from flask import render_template,request    



@crawl.route('/',methods=['GET'])
def crawl_main():
    return render_template('crawl.html')
@crawl.route('/',methods=['POST'])
def data_load():
    data = request.form
    print(request.form)
    in_name = data.get()
    main1(mode=data.get('model'), out_path='./static/out/', tune= )
    return data;




    
