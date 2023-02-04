FROM python:3.8-slim-buster

WORKDIR /api_sync

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY runner.py .
COPY endpoints/. endpoints/.
COPY interface/. interface/.
COPY util/. util/.

CMD [ "python3", "runner.py"]
