FROM python:3.11 as base

RUN apt update && apt install -y build-essential curl vim fish git sudo \
    && groupadd -g 1000 docker-user \
    && useradd -d /home/docker-user -s /bin/bash -u 1000 -g 1000 docker-user \
    && usermod -aG sudo docker-user && echo "docker-user:1234" | sudo chpasswd \
    && mkdir /home/docker-user \
    && chown -R docker-user:docker-user /home/docker-user

USER docker-user

RUN python -m pip install Django

# FROM base AS dev

# FROM base AS prod