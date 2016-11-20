FROM mhart/alpine-node
MAINTAINER Ruben Vasconcelos

EXPOSE  8000

# Update
RUN apk add --update \
    python \
    py-pip \
    git

# Install bower
RUN npm install -g bower

# Install app dependencies
COPY ./application/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt && \
    rm -rf /tmp/*

#Create appuser
RUN addgroup appuser && \
    adduser -s /bin/sh -D -G appuser appuser

WORKDIR /src/keeperoo

USER appuser
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
