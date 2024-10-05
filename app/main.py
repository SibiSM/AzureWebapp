from flask import Blueprint, render_template, request, redirect, url_for
from azure.storage.blob import BlobServiceClient
from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging
import os
from . import db

# Load environment variables from .env file

main = Blueprint('main', __name__)

# Azure Blob Storage details
storage_account_name = 'storageblobsibi'
# Access storage account key from environment variable
storage_account_key = 'gTbz2GWnr0uXAOQdZSCmB05xCz5qVm9sHFE1ONUl7/h7oWIcXjvXC6NfLMTTmXNp+NSi0xIBJAFP+AStjiSsPQ=='
container_name = 'containerstorage'

connect_str = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={storage_account_key};EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Application Insights setup
instrumentation_key = '710443bc-9d4e-43a4-9674-7d889501eaa5'  # Replace with your actual instrumentation key
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string=f'InstrumentationKey={instrumentation_key}'))

@main.route('/')
def index():
    logger.info('Index page accessed')
    return render_template('index.html', title="Welcome to Sibi's Web Application")

@main.route('/about')
def about():
    logger.info('About page accessed')
    return render_template('about.html', title="About This Web App")

@main.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file.filename)
        blob_client.upload_blob(file)
        logger.info(f'File uploaded: {file.filename}')
        return redirect(url_for('main.upload_success', filename=file.filename))

@main.route('/upload_success')
def upload_success():
    filename = request.args.get('filename')
    logger.info(f'Upload successful: {filename}')
    return render_template('upload_success.html', filename=filename, title="Upload Success")
