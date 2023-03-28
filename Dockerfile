FROM node:19.8.1-alpine3.17

RUN apk add --no-cache python3 python3-dev \
    linux-headers build-base bash git ca-certificates && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools==45 && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache

WORKDIR /app

# RUN apk add --update nodejs

# Copy the requirements file first, to take advantage of Docker's caching mechanism
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# Copy the rest of the app code
COPY ./pynecone .
COPY .env ../

# RUN ["cd", "pynecone"]
CMD ["bash", "run.sh"]
