from flask import Flask, request, render_template
from flask_cors import CORS
import fake_news as FNP

app=Flask(__name__)

CORS(app)

@app.route("/")
def get():
    return render_template('index.html', LR="", DT="", GB="", RF="")

@app.route("/predict", methods=['POST'])
def send():
    text=request.form['title']
    x=FNP.manual_testing(text)
    return render_template('index.html', LR=x["logisticRegression"], DT=x["DecisionTree"], GB=x["GradientBoosting"], RF=x["RandomForest"])

if __name__=='__main__':
    app.run(debug=True)