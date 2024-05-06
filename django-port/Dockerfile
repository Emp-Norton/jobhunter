# Use an official Python image as a base
FROM python:3.8.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app

# Install the dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code
COPY . /app

# Expose the port the application will use
EXPOSE 8000

# Run the command to start the development server when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
