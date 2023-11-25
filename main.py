from flask import Flask, request, render_template
from flask_cors import CORS
from joblib import load
import pandas as pd
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

app=Flask(__name__)

CORS(app)

vectorization = TfidfVectorizer()

def wordopt(text):
    text = text. lower()
    text = re.sub('\[ .*? \]', '', text)
    text = re.sub("\\W", " ", text)
    text = re.sub('https ?: //\S+|www\.\S+', '', text)
    text = re.sub(' <.*? >+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# data_fake = pd.read_csv('Fake.csv')
# data_true = pd.read_csv('True.csv')
# data_fake["class"] = 0
# data_true["class"] = 1

# data_fake_manual_testing = data_fake.tail(10)
# for i in range(23480, 23470, -1):
#     data_fake.drop([i], axis = 0, inplace = True)

# data_true_manual_testing = data_true.tail(10)
# for i in range(21416, 21406, -1):
#     data_true.drop([i], axis = 0, inplace = True)

# data_fake_manual_testing["class"] = 0
# data_true_manual_testing["class"] = 1

# data_merge = pd.concat([data_fake, data_true], axis = 0)
# data = data_merge.drop(["subject", "date"], axis = 1)
# data = data.sample(frac = 1)
# data.reset_index(inplace = True)
# data.drop(['index'], axis = 1, inplace = True)
# data['title'] = data['title'].apply(wordopt)
# x = data['title']
# y = data['class']
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)

# xv_train = vectorization.fit_transform(x_train)
# xv_test = vectorization.transform(x_test)

LR=load('LR.joblib')
DT=load('DT.joblib')
GB=load('GB.joblib')
RF=load('RF.joblib')

def output_lable(n):
    if n == 0:
        return "Fake News"
    elif n == 1:
        return "Not A Fake News"

def manual_testing(news: str):
    testing_news = {"text": [news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(wordopt)
    new_x_test = new_def_test["text"]
    new_xv_test = vectorization.transform(new_x_test)
    pred_LR = LR.predict(new_xv_test)
    pred_DT = DT.predict(new_xv_test)
    pred_GB = GB.predict(new_xv_test)
    pred_RF = RF.predict(new_xv_test)
    # return pred_DT
    return ("\n\nLR Prediction: {} \nDT Prediction: {} \nGB Prediction: {} \nRF Prediction: {}".format(output_lable(pred_LR[0]), output_lable(pred_DT[0]), output_lable(pred_GB[0]), output_lable(pred_RF[0])))

@app.route("/")
def get():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def send():
    text=request.form['title']
    print(text)
    # return text.upper()
    return manual_testing(text)


if __name__=='__main__':
    app.run(debug=True)