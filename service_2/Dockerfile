FROM python:latest

RUN mkdir service2
COPY . /service2/
WORKDIR /service2/
RUN apt-get update -y
RUN apt-get install python3-venv -y
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt

ENTRYPOINT python3 app.py