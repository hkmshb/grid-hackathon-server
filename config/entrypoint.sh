#!/usr/bin/env bash
set -e

# Define help message
show_help() {
  echo """
  Commands
  start         : start application server
  bash          : start bash shell
  manage        : run a flask management command
  """
}

case "$1" in
  start )
    aws s3 cp --sse AES256 s3://ecs-secrets-$ENV/$PROJECT - > ~/.env
    source ~/.env
    /usr/local/bin/uwsgi --ini /app/config/uwsgi.ini
  ;;
  start_dev )
    /usr/local/bin/uwsgi --ini /app/config/uwsgi.ini
  ;;
  bash )
    /bin/bash
  ;;
  manage )
  cd /app
    python manage.py "${@:2}"
  ;;
  * )
    show_help
  ;;
esac
