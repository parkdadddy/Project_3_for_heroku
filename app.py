# import necessary libraries
# from models import create_classes
import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template,request
from flask_sqlalchemy import SQLAlchemy



#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy


#flask
app = Flask(__name__)
app.config['JSON_SORT_KEYS']= False

# db = SQLAlchemy(app)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/index.html")
def homepage():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/Rent.html")
def Rent():
    return render_template("Rent.html")

@app.route("/Education.html")
def Education():
    return render_template("Education.html")

@app.route("/Income.html")
def Income():
    return render_template("Income.html")

@app.route("/Household.html")
def Household():
    return render_template("Household.html")

# @app.route("/Methodology.html")
# def Methodology():
#     return render_template("Methodology.html")

@app.route("/Housing_predic.html")
def Housing_predic():
    return render_template("Housing_predic.html")


if __name__ == "__main__":
    app.run()
