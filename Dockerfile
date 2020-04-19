FROM python:slim

ENV PYTHONUNBUFFERED=1

ADD ./ /

RUN python3 -m venv venv
RUN . /venv/bin/activate
RUN pip3 install -r requirements.txt

CMD ["python3", "dtp_bot.py"]