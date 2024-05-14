FROM python:3.10.6

RUN apt update
RUN apt-get install -y uvicorn

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY models models
COPY app.py app.py

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
