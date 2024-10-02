from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
import logging

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Integrate Application Insights
    connection_string = "InstrumentationKey=710443bc-9d4e-43a4-9674-7d889501eaa5;IngestionEndpoint=https://eastus-8.in.applicationinsights.azure.com/;LiveEndpoint=https://eastus.livediagnostics.monitor.azure.com/;ApplicationId=b2256d6c-2a0b-4da7-8123-3cfab3279323"

    # Logger configuration for Azure Application Insights
    logger = logging.getLogger(__name__)
    logger.addHandler(AzureLogHandler(connection_string=connection_string))
    logger.setLevel(logging.INFO)

    # Middleware for tracking Flask requests
    FlaskMiddleware(app, exporter=AzureExporter(connection_string=connection_string), sampler=ProbabilitySampler(1.0))

    return app, logger
