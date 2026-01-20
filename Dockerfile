FROM python:3.12.1

ADD main.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]