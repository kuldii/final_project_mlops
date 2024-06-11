import re
import joblib
import streamlit as st
import plotly.graph_objects as go

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
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


options = ['Random Forest', 'Gradient Boosting']


# Define the Streamlit app
def main():
    # Set the title of the app
    st.title("Text Classification App")

    selected_option = st.selectbox('Select Model:', options)

    # Load the model from the joblib file
    model = joblib.load(
        'model/gradient_boosting_model.pkl'
        if selected_option == 'Gradient Boosting'
        else 'model/random_forest_model.pkl')

    # Add a text input field for user input
    user_input = st.text_input("Enter text:")

    # Add a button to trigger predictions
    if st.button("Predict"):
        # Preprocess the user input
        processed_input = preprocess_text(user_input)

        if processed_input:
            # Perform prediction using the loaded model
            prediction = model.predict([processed_input])
            prediction_proba = model.predict_proba([processed_input])

            # Display the prediction result
            st.header("Result :")
            st.write(f"Prediction: {prediction[0]}")

            classes = model.classes_
            probabilities = prediction_proba[0]
            colors = ['lightskyblue' if prob != max(probabilities)
                      else 'lightcoral' for prob in probabilities]

            fig = go.Figure(data=[
                go.Bar(x=classes, y=probabilities, marker_color=colors)
            ])

            fig.update_layout(title='Prediction Probabilities',
                              xaxis_title='Class', yaxis_title='Probability')
            st.plotly_chart(fig)
        else:
            st.write("Please enter valid text for prediction.")


# Run the app
if __name__ == "__main__":
    main()
