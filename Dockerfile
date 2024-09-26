# Use the official Python image
FROM python:3.8-slim

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    curl \
    gnupg \
    apt-transport-https

# Add Microsoft repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list -o /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update

# Install ODBC Driver 17 for SQL Server and dependencies
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "uploads/app.py"]
