
from flask import Flask, request ,render_template
from pymongo import MongoClient

cluster = "mongodb+srv://Reem:d0vniEkL7wMyD1X4@cluster0.jaez9.mongodb.net/ShortenerUrl_DB?retryWrites=true&w=majority"
client = MongoClient(cluster)

print(client.list_database_names())
db= client.test
app = Flask(__name__)
@app.python 
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
