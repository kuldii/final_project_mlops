import re
import joblib
import pandas as pd

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.metrics import classification_report

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    if isinstance(text, str):
        text = text.lower()
        text = re.sub(r'\d+', '', text)
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        tokens = word_tokenize(text)
        filtered_tokens = [
            lemmatizer.lemmatize(word) for word in tokens
            if word not in stop_words]
        return ' '.join(filtered_tokens)
    else:
        return ''


df = pd.read_csv('data/twitter_validation.csv',
                 names=['id', 'entity', 'sentiment', 'content'])

df.dropna(axis=0, inplace=True)

df['cleaned'] = df['content'].apply(preprocess_text)

df = df[df['cleaned'] != ""]
df.drop_duplicates(inplace=True)

X_test = df['cleaned']
y_test = df['sentiment']

# Load the model from the file
model = joblib.load('model/random_forest_model.pkl')

# Validation Model
y_pred = model.predict(X_test)

# Evaluate Model
print(classification_report(y_test, y_pred,
                            target_names=['Positive', 'Negative',
                                          'Neutral', 'Irrelevant']))
