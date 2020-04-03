FROM python:latest

RUN mkdir service3
COPY . /service3/
WORKDIR /service3/
RUN apt-get update -y
RUN apt-get install python3-venv -y
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt

ENTRYPOINT python3 app.py