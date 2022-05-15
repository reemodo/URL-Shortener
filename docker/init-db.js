 db = db.getSiblingDB("urlshortener");
 db.url.drop();
 db.animal_tb.insertMany([
    {
        "id": 1,
        "originalURL": "https://github.com/ashutosh1919/flask_mongodb_dockerized_app/blob/master/init-db.js",
        "shortURL": "https://localhost:5002",
        "creationDate":new Date(),
        "userID": 1
    }])
