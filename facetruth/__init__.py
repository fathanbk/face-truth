import os

from flask import Flask, current_app, render_template, make_response, jsonify, request, flash, redirect, send_file
from flask_cors import CORS
from facetruth.db import DB
from facetruth.processing import lie_detect


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=DB('localhost', 27017, 'face_truth'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def index():
        lie_detect(["D:\Download\output.mp4"])
        return "test"

    return app