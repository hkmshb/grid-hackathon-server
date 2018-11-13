#!/bin/bash

set -ex

export AWS_DEFAULT_REGION="eu-west-1"
export IMAGE_REPO="387526361725.dkr.ecr.eu-west-1.amazonaws.com"
export APP="grid3-hackserver-api"


if [ "${TRAVIS_BRANCH}" == "conf/deployment" ] && [ "${TRAVIS_PULL_REQUEST}" == "false" ]; then
  $(aws ecr get-login --region="${AWS_DEFAULT_REGION}" --no-include-email)
  export ENV="prod"
fi

if [ "${ENV}" == "prod" ]; then
    CLUSTER_NAME="ehealth-africa"

    # build and push nginx container
    docker build -t "${IMAGE_REPO}/${APP}-nginx-${ENV}:latest" nginx/.
    docker push "${IMAGE_REPO}/${APP}-nginx-${ENV}:latest"

    # build and push api
    docker build -t "${IMAGE_REPO}/${APP}-${ENV}:latest" .
    docker push "${IMAGE_REPO}/${APP}-${ENV}:latest"

    # ecs deploy
    ecs deploy --timeout 600 ${CLUSTER_NAME}-${ENV} ${APP}
fi
