#!/bin/bash
virtualenv venv --python=3.8
source ./venv/bin/activate
pip3 install Flask
pip3 install Flask-JWT
pip3 install Flask-RESTful