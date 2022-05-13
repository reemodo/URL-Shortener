

from flask import Flask, redirect, request ,render_template 
from database.db import db
from database.url import url
import base64
db.initialize()
app = Flask(__name__)


def idToShortURL(id): 
    encoded = base64.b64encode(id.encode('ascii'))
    return str(encoded)



@app.route('/',methods=['POST','GET'])
def main():
    if request.method == "POST" :
        insertedURL = request.form["url"]
        dbContainURL = url.objects(originalURL = insertedURL).first()
        if dbContainURL == None:
            urlone=url()
            shortenerURL =   idToShortURL(insertedURL )
            urlone.originalURL =insertedURL
            urlone.shortURL =shortenerURL
            urlone.save()
            #shortenerURL =   idToShortURL(urlone._id)
            return render_template('MainHtml.html',short_url =request.host_url+shortenerURL)
        else :
            return render_template('MainHtml.html',short_url =request.host_url+dbContainURL.shortURL)
            
    else :
        return render_template('MainHtml.html')

@app.route('/<short_id>')
def redirects(short_id):
    urlexist = url.objects(shortURL = short_id).first()
    if urlexist :
        return redirect(urlexist.originalURL)
    else :
        return '<h1>about page<h1>'

if __name__ == '__main__' :
    app.run(debug = True)


