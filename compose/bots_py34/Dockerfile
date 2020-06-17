FROM python:3.4-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && apk upgrade
RUN apk add build-base postgresql-dev

COPY ./etc /requirements

RUN pip install -r /requirements/requirements.txt

COPY . /bots
RUN pip install /bots
RUN cd .. && rm -rf /bots

# clean up
Run apk del --purge --force linux-headers \
    binutils-gold gnupg libc-utils libstdc++ \
    libxml2-dev libxslt-dev \
    libjpeg-turbo-dev libpng-dev \
    freetype-dev lcms2-dev libwebp-dev \
    harfbuzz-dev fribidi-dev tcl-dev tk-dev

EXPOSE 8080
