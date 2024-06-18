FROM python:3.10-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Run the django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

