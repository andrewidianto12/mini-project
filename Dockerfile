# Use an official Python runtime as a parent image
FROM python:3.10-slim

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

# Install any needed dependencies specified in requirements.txt
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["python", "run", "--host", "0.0.0.0"]
