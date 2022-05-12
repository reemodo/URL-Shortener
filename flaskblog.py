

from flask import Flask, request ,render_template 
from pymongo import MongoClient
import database.db 

mydb = database.db.iniDB()
app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def hello():
    if request.method == "POST" :
        urlLogn = request.form["urlLogn"]
        if urlLogn == '' :
            shortURL = "http://127.0.0.1:5000/" + "short"
            mycol= mydb.Usrers
            mydict = { "name": "shortURL", "address": "Highway 37" }
            x = mycol.insert_one(mydict)
            return (x.inserted_id)
    else :
        return render_template('MainHtml.html')

@app.route('/about')
def about():
    return '<h1>about page<h1>'

if __name__ == '__main__' :
    app.run(debug = True)
