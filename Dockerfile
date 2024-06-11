FROM python:3.8-slim

WORKDIR /app

COPY . /app
COPY ./model /app/model

RUN pip install --no-cache-dir --upgrade pip setuptools

RUN python -m pip install scikit-learn==1.2.2
RUN python -m pip install streamlit
RUN python -m pip install joblib==1.2.0
RUN python -m pip install nltk
RUN python -m pip install plotly

RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader stopwords

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
