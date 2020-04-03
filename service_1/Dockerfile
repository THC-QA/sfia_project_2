FROM python:latest

RUN mkdir service1
COPY . /service1/
WORKDIR /service1/
RUN apt-get update -y
RUN apt-get install python3-venv -y
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT python3 app.py