FROM python:3.10-slim-bullseye

WORKDIR /usr/src/app

COPY . .

RUN apt-get -y update 
RUN apt-get install build-essential -y
RUN pip install --upgrade pip

RUN apt install lsb-release -y

RUN pip install gunicorn uvicorn
RUN pip install -r requirements.txt

# Remova a linha "COPY create_superuser.py /usr/src/app/"

RUN chmod +x ./prestart.sh

ENV DEBUG=0

CMD ["./prestart.sh"]
