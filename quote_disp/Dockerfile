# Use the official Python image with tag 3.8-slim-buster as the base image
FROM python:3.8-slim-buster

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Specify the command to run on container start
ENTRYPOINT ["python"]

# Specify the default argument for the entrypoint
CMD ["app.py"]
