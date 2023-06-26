FROM python:3.11.4-bookworm

#disable pip cache because we aren't going to need it, 
#and make it so that log messages show up immediately.
#This follows instructions on
# https://medium.com/vantageai/how-to-make-your-python-docker-images-secure-fast-small-b3a6870373a0

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN set -ex \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN set -ex \
    && mkdir /dighum150a \
    && mkdir /dighum150a/demos \
    && mkdir /dighum150a/docs
    

#copy in demo code.
WORKDIR /dighum150a
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./demos demos/
COPY ./docs docs/


#run a local webserver with help documents. It keeps the container running
#while providing helpful information.
EXPOSE  8000
CMD python -m http.server 8000 --directory docs/
