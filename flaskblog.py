from flask import Flask, request ,render_template
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def hello():
    if request.method == "POST" :
        urlname = request.form["nm"]
        return urlname
    else :
        return render_template('MainHtml.html')

@app.route('/about')
def about():
    return '<h1>about page<h1>'

if __name__ == '__main__' :
    app.run(debug = True)
