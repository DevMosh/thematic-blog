FROM python:3.12

# /bin/bash -c - тоже самое, что и RUN
SHELL ["/bin/bash", "-c"]

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "blog.wsgi:application" ]
