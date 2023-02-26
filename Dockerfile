FROM python:3.10.8

WORKDIR /code

COPY ./prod_dockerfile/web/requirements.txt .

RUN pip install -r ./requirements.txt

COPY src/ .

EXPOSE 8000

CMD [ "gunicorn", "-w" ,"4" ,"--bind", "0.0.0.0:8000", "api:app" ]