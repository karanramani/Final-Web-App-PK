FROM python:3.8

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install  -r requirements.txt --upgrade pip
RUN pip install Flask-Mail
RUN pip install python-dotenv

COPY . /app

CMD python app.py