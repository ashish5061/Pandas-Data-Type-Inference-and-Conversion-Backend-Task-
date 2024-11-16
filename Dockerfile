# Specify the base image
FROM python:3.13.0-bullseye

# Prevents Python from buffering stdout and stderr, useful for logging in Docker
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /backend

# Copy requirements file if you have one, to install dependencies separately (optional)
 COPY requirements.txt ./
 RUN pip install -r requirements.txt


# Copy all files from the current directory to the WORKDIR in the container
COPY . .

# Expose port 8000 for Django development server
EXPOSE 8000

# Set the default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

