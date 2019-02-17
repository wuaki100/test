from  flask import  Flask,jsonify,render_template,request,url_for
import userlocal

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('province.html')




@app.route('/province',methods=['POST','GET'])
def province():

    rev=request.get_json()['city']
    print(rev)
    result=({'1':'深圳','2':'惠州','3':'广州','4':'雷州','5':'韶关','6':'清远'})
    return  jsonify(result)

@app.route('/login',methods=['POST','GET'])
def login():
    name=request.get_json()['name']
    if name == '11':
        result = [{"name":"厦门"},{"name":"深圳"},{"name":"成都"},{"name":"重庆"}]
    else:
        result = [{"name": "不存在"} ]
    return  jsonify(result)



@app.errorhandler(404)
def page_not_found(e):
    res = {'error': 'not found'}
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0')