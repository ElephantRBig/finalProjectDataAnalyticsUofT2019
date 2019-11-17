from flask import Flask, render_template, escape, url_for
import json

app = Flask(__name__)

@app.route('/')
def echo():
    # Import our pymongo library, which lets us connect our Flask app to our Mongo database.
    import pymongo

    # Setup connection to mongodb
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)

        # Select database and collection to use
    db = client.marsScrape
    collection = db.collection
    data = collection.find({})[0]
    return render_template("index.html", data = data)


#===================================================
if __name__=="__main__":
    app.run(debug=True)