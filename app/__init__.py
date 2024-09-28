from flask import Flask,jsonify,request
from apispec import APISpec
from flask_restful import Resource, Api
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_cors import CORS
from app import utility
from app import schema

application= Flask(__name__)
application.secret_key='dcs-1234' 

CORS(application)
api=Api(application)

application.config.update({
    'APISPEC_SPEC': APISpec(
        title='DCS Generate Doc',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'),
        'APISPEC_SWAGGER_URL':'/swagger/',
        'APISPEC_SWAGGER_UI_URL':'/swagger-ui/'
})
docs=FlaskApiSpec(application)

@application.route("/")
def generate_document():
    return "Welcome to DCS Swagger-ui to get help with Document Generation"
