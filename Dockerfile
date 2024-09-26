# Use the official Python image
FROM python:3.8-slim

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    curl \
    gnupg \
    apt-transport-https && \
    apt-get clean

# Add Microsoft repository for ODBC Driver 17
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list -o /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update

# Install ODBC Driver 17 for SQL Server and dependencies
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev

# Install OpenGL and other necessary libraries for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask application
EXPOSE 5000

# Run the Flask application
CMD ["python", "uploads/app.py"]
