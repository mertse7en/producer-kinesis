FROM python:3.7

RUN apt update
RUN pip install --upgrade pip

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/.








ENTRYPOINT [ "python", "-u", "run.py"]