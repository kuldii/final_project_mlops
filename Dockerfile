FROM python:3.8-slim

WORKDIR /app

COPY . /app
COPY model /app/model

RUN pip install --no-cache-dir --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt -v
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader stopwords

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
