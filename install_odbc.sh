#!/bin/bash

# Update the package list
apt-get update

# Install curl and other dependencies
apt-get install -y curl apt-transport-https gnupg2

# Import the public repository GPG keys
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Register the Microsoft SQL Server Ubuntu repository
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Update the package list again to include the new repository
apt-get update

# Install the ODBC Driver 17 for SQL Server and unixODBC development libraries
ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev

# Clean up to save space
apt-get clean -y
rm -rf /var/lib/apt/lists/*
pip install -r requirements.txt