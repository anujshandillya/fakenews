from flask import Flask, request
from flask_cors import CORS
import datetime

time=datetime.datetime.now()

app=Flask(__name__)

CORS(app)

@app.route("/")
def get():
    return {
        "name": "Anuj Sharma",
        "date": time
    }

@app.route("/predict", methods=['POST'])
def send():
    request.content_type('application/json')
    news = request.json('news')
    return news


if __name__=='__main__':
    app.run(debug=True)