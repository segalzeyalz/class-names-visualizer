FROM --platform=linux/amd64 python:3.8.6
COPY requirements.txt .

RUN apt-get update \
    && apt-get install -y curl apt-transport-https \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev

RUN pip install -r requirements.txt --ignore-installed

WORKDIR /app
COPY . /app

CMD gunicorn -w 4 app:app -b :8000