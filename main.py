from flask import Flask
import datetime

time=datetime.datetime.now()

app=Flask(__name__)

@app.route("/")
def get():
    return {
        "name": "Anuj Sharma",
        "date": time
    }


if __name__=='__main__':
    app.run(debug=True)