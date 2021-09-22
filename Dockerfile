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

#RUN touch /usr/cronjobs/scripts/log/01_get_api.log && touch /usr/cronjobs/scripts/log/cronjobs.log
RUN touch /usr/cronjobs/scripts/log/cronjobs.log

CMD cron && tail -f /usr/cronjobs/scripts/log/cronjobs.log