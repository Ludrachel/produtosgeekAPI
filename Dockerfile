FROM python:3.12

WORKDIR /home/app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "fastapi", "run", "server.py" ]