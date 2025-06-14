# Dockerfile
# This line specifies the base image we'll start from.
# python:3.9-slim-buster means a Python 3.9 environment on a Debian Buster Linux distribution.
FROM python:3.9-slim-buster

# This sets the working directory inside the Docker image.
# All subsequent instructions (like COPY, RUN) will be relative to this directory.
WORKDIR /app

# This copies your 'app.py' file from your local computer into the '/app' directory inside the Docker image.
COPY app.py .

# This command runs inside the Docker image during the build process.
# It installs the 'Flask' library, which our app.py needs to run.
RUN pip install Flask

# This informs Docker that the container will listen on port 5000 at runtime.
# It's documentation; it doesn't actually publish the port. That's done when running the container.
EXPOSE 5000

# This specifies the command that will be executed when a container starts from this image.
# It tells the container to run your Python application.
CMD ["python", "app.py"]
