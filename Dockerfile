# Use the official Python image 
FROM python:3.9

# Set the working directory
WORKDIR /app

#Copy application code
COPY app.py /app/app.py

# Set the default command to run application
CMD ["python", "/app/app.py"]
