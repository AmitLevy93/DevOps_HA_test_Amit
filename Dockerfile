FROM python:3
WORKDIR /app
COPY flask_sample_web_app.py /app/
CMD "python3 flask_sample_web_app.py"