import pandas as pd
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

newsFake=pd.read_csv("Fake.csv", low_memory=False)
newsTrue=pd.read_csv("True.csv", low_memory=False)
newsFake['class']=0
newsTrue['class']=1

model=DecisionTreeClassifier()

def txtprcs(text):
    # convert to lower case.
    text=text.lower()
    # Remove text between square brackets, like [text]
    text = re.sub('\[.*?\]', '', text)
    # Replace non-word characters (punctuation, symbols) with spaces
    text = re.sub("\\W", " ", text)
    # Remove URLs starting with 'http://' or 'https://' and 'www.'
    text = re.sub('https?://\S+|www\.\S+', '', text)
    # Remove HTML tags
    text = re.sub('<.*?>+', '', text)
    # Remove all punctuation characters
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    # Remove newline characters
    text = re.sub('\n', '', text)
    # Remove words containing digits (e.g., 'word123')
    text = re.sub('\w*\d\w*', '', text)
    
    return text

merged_news=pd.concat([newsTrue,newsFake])
merged_news.dropna(inplace=True)
merged_news.isna().sum()
merged_news[['text','class']]

X=merged_news['title']
y=merged_news['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

vect=TfidfVectorizer()
xv_train=vect.fit_transform(X_train)
xv_test=vect.transform(X_test)

model.fit(xv_train, y_train)
predict=model.predict(xv_test)