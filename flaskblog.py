

from flask import Flask, redirect, request ,render_template 
from database.db import db
from database.url import url
import base64
db.initialize()
app = Flask(__name__)


def idToShortURL(id): 
    encoded = base64.b64encode(id.encode('ascii'))
    return str(encoded)




def shortURLToId(shortURL):
    id = 0
    for i in shortURL:
        val_i = ord(i)
        if(val_i >= ord('a') and val_i <= ord('z')):
            id = id*62 + val_i - ord('a')
        elif(val_i >= ord('A') and val_i <= ord('Z')):
            id = id*62 + val_i - ord('Z') + 26
        else:
            id = id*62 + val_i - ord('0') + 52
    return id
@app.route('/',methods=['POST','GET'])
def main():
    if request.method == "POST" :
        insertedURL = request.form["url"]
        dbContainURL = url.objects(originalURL = insertedURL).first()
        if dbContainURL == None:
            urlone=url()
            shortenerURL =   idToShortURL(urlone.objectId().str )
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


