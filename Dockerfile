FROM alpine:3.17.2
RUN apk add --no-cache wget
RUN apk update && apk add wget
RUN apk add --no-cache python3 python3-dev py3-pip\
    linux-headers build-base bash git ca-certificates && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools==45 && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache
RUN apk add --update nodejs
RUN apk add --update npm

WORKDIR /app

# RUN apk add --update nodejs

# Copy the requirements file first, to take advantage of Docker's caching mechanism
RUN python - m pip install – upgrade pip
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# Copy the rest of the app code
COPY ./pynecone .
COPY .env ../

# RUN ["cd", "pynecone"]
CMD ["bash", "run.sh"]
