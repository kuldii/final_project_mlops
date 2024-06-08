import re
import joblib
import streamlit as st

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

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


# Load the model from the joblib file
model = joblib.load('model/random_forest_model.pkl')


# Define the Streamlit app
def main():
    # Set the title of the app
    st.title("Text Classification App")

    # Add a text input field for user input
    user_input = st.text_input("Enter text:")

    X_test = preprocess_text(user_input)

    # Add a button to trigger predictions
    if st.button("Predict"):
        # Perform prediction using the loaded model
        prediction = model.predict([X_test])

        # Display the prediction result
        st.write("Prediction:", prediction[0])


# Run the app
if __name__ == "__main__":
    main()
