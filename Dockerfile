FROM python:3.8-alpine

ENV PYTHONPATH $PYTHONPATH:/app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app/

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]