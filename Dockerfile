FROM python:slim

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /app
ADD ./ /app
WORKDIR /app

RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt

RUN useradd user
USER user

CMD ["python3", "dtp_bot.py"]
