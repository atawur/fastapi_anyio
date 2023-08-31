FROM python:3.11.3-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# setting a working directory in the container
WORKDIR /code

# Copy requirements from host, to docker container work directory
COPY ./requirements.txt /code/requirements.txt


# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy everything from host /app directory to docker container /app directory
COPY ./app ./app

# Run the application in the port 8000
#CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "app.main:app"]
