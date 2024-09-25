#!/bin/bash

# Update system and install necessary packages
apt-get update

# Install unixODBC (required by pyodbc)
apt-get install -y unixodbc-dev curl apt-transport-https

# Import Microsoft GPG keys and add repository
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | tee /etc/apt/sources.list.d/msprod.list

# Install ODBC Driver 17 for SQL Server
apt-get update
ACCEPT_EULA=Y apt-get install -y msodbcsql17

 pip install -r requirements.txt