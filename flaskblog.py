from flask import Flask,request

app = Flask(__name__)


@app.route('/',methods=['POST','GET')
def hello():
    if request.method == "POST" :
        return true
    return '<h1>home  page<h1>'

@app.route('/about')
def about():
    return '<h1>about page<h1>'

if __name__ == '__main__' :
    app.run(debug = True)
