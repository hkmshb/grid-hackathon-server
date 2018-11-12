FROM python:3.6

RUN apt-get update
RUN mkdir /app
WORKDIR /app

ADD . /app
ADD config/entrypoint.sh /tmp/entrypoint.sh
RUN chmod +x /tmp/entrypoint.sh
RUN pip install poetry awscli
RUN poetry config settings.virtualenvs.create false
RUN poetry install
EXPOSE 5000
ENTRYPOINT [ "/tmp/entrypoint.sh" ]
