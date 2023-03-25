FROM python:3.10.9

WORKDIR /app

# RUN apk add --update nodejs

# Copy the requirements file first, to take advantage of Docker's caching mechanism
COPY requirements.txt .
RUN pip install -r requirements.txt


# Copy the rest of the app code
COPY ./pynecone .
COPY .env ../

# RUN ["cd", "pynecone"]
CMD ["bash", "run.sh"]
