# Pulling the python image
FROM python:3.8-alpine

# Copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# Switch working directory
WORKDIR /app

# Install all the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# Copy every content from the local file to the image
COPY . /app

# Define environment variable to check if the code runs from a docker container
ENV AM_I_IN_A_DOCKER_CONTAINER Yes

# Run flask_web_app.py when the container launches
ENTRYPOINT ["python"]
CMD ["flask_web_app.py"]