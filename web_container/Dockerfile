FROM python:3.9.15-alpine

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev postgresql-dev libxml2 libxslt-dev libmagic libpq-dev python3-dev
RUN python -m pip install -r /code/requirements.txt --no-cache-dir

# copy entrypoint.sh
COPY entrypoint.sh .
RUN sed -i 's/\r$//g' /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]