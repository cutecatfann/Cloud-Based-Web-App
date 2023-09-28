# Use the Python version of alpine as the base image
FROM python:alpine

# Specify your e-mail address as the maintainer of the container image
MAINTAINER YOUR NAME "yourname@gmail.com"

# Copy the contents of the current directory into the container directory /app
COPY . /app

# Set the working directory of the container to /app
WORKDIR /app

# Install the Python packages specified by requirements.txt into the container
RUN pip install --no-cache -r requirements.txt

# Set the program that is invoked upon container instantiation
ENTRYPOINT ["python"]

# Set the parameters to the program
CMD ["app.py"]
