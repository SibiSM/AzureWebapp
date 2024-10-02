from flask import Blueprint, render_template, request, redirect, url_for
from azure.storage.blob import BlobServiceClient
<<<<<<< HEAD
from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging
import os
from . import db

# Load environment variables from .env file
=======
import logging
>>>>>>> f9194e8 (new)

main = Blueprint('main', __name__)

# Azure Blob Storage details
storage_account_name = 'storageblobsibi'
<<<<<<< HEAD
# Access storage account key from environment variable
storage_account_key = 'Ig/VgQNy+l9ts4NNZ/yqyGItfMBnO/QgbwMkX86P9yAxyUJSfsazonsn5EYU0UFEU1UfYAA6tiFT+AStZWUuQQ=='
=======
storage_account_key = 'Ig/VgQNy+l9ts4NNZ/yqyGItfMBnO/QgbwMkX86P9yAxyUJSfsazonsn5EYU0UFEU1UfYAA6tiFT+AStZWUuQQ=='  # Replace with your actual key
>>>>>>> f9194e8 (new)
container_name = 'containerstorage'

connect_str = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={storage_account_key};EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

<<<<<<< HEAD
# Application Insights setup
instrumentation_key = '710443bc-9d4e-43a4-9674-7d889501eaa5'  # Replace with your actual instrumentation key
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string=f'InstrumentationKey={instrumentation_key}'))

@main.route('/')
def index():
    logger.info('Index page accessed')
=======
# Get the logger instance
logger = logging.getLogger(__name__)

@main.route('/')
def index():
    logger.info("Index page loaded")
>>>>>>> f9194e8 (new)
    return render_template('index.html', title="Welcome to Sibi's Web Application")

@main.route('/about')
def about():
<<<<<<< HEAD
    logger.info('About page accessed')
=======
    logger.info("About page loaded")
>>>>>>> f9194e8 (new)
    return render_template('about.html', title="About This Web App")

@main.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file.filename)
        blob_client.upload_blob(file)
<<<<<<< HEAD
        logger.info(f'File uploaded: {file.filename}')
=======
        logger.info(f"File uploaded: {file.filename}")
>>>>>>> f9194e8 (new)
        return redirect(url_for('main.upload_success', filename=file.filename))

@main.route('/upload_success')
def upload_success():
    filename = request.args.get('filename')
<<<<<<< HEAD
    logger.info(f'Upload successful: {filename}')
=======
    logger.info(f"Upload successful: {filename}")
>>>>>>> f9194e8 (new)
    return render_template('upload_success.html', filename=filename, title="Upload Success")
