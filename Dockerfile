FROM python:3.9
WORKDIR /app
RUN apt update
RUN apt-get install -y libsndfile1
COPY ./requirements.txt /app/requirements.txt
COPY .env /app/.env
RUN pip install -r /app/requirements.txt
COPY . /app

ENTRYPOINT ["python"]

CMD ["main.py"]