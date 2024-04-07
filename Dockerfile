# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /code/data

# Copy the current directory contents into the container at /app
COPY /data/test.csv /data/train.csv /code/data/
# Set the working directory inside the container
WORKDIR /code
# Copy the current directory contents into the container at /code
COPY train.py test.py requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Train your model (replace with actual training commands)
RUN python train.py

# Specify the command to execute when the container starts
CMD ["python", "test.py"]
