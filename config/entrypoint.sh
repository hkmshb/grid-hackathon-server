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
  start)
    cd /app
    python manage.py run -h 0.0.0.0
  ;;
  bash )
    /bin/bash
  ;;
  manage)
  cd /app
    python manage.py "${@:2}"
  ;;
  *)
    show_help
  ;;
esac
