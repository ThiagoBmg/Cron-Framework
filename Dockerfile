FROM ubuntu:latest

RUN apt update && apt install \ 
    cron -y \
    python -y \
    pip -y \ 
    python3.8-venv

ADD ./config/crontab /etc/cron.d/cronjobs

COPY ./cronjobs /usr/cronjobs/scripts/
COPY ./requirements.txt /usr/cronjobs/requirements.txt

RUN  pip install -r /usr/cronjobs/requirements.txt

RUN touch /var/log/01_get_api.log

CMD cron && tail -f /var/log/01_get_api.log