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
engine = create_engine("sqlite:///gentrification.db")

Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Data = Base.classes.gentrification

# session = Session(engine)
# inspector = inspect(engine)
# inspector.get_table_names()

# session = Session(engine)
# print("-----------------------")

# print(session)
# results = session.query(*crash).filter(Data.YEAR == year).all()
# results = session.query(*Gentrification).all()


#flask
app = Flask(__name__)
app.config['JSON_SORT_KEYS']= False

# db = SQLAlchemy(app)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("Landing.html")


@app.route("/Rent.html")
def Rent():
    return render_template("Rent.html")




# @app.route("/data")
# def data():

   
#     print("********************")
#     print(Data)

#     """Return the MetaData for a given sample."""
#     Gentrification = [
#     Data.id,
#     Data.SA2_Code,
#     Data.SA2_Name,
#     Data.Rent_2006,
#     Data.Rent_2011,
#     Data.Rent_2016,
#     Data.Rent_per_2006_2011,
#     Data.Rent_per_2011_2016,
#     Data.Rent_per_2006_2016,
#     Data.House_avg2006,
#     Data.House_avg2011,
#     Data.House_avg2016,
#     Data.House_per_2006_2011,
#     Data.House_per_2011_2016,
#     Data.House_per_2006_2016,
#     Data.Income_total_2006,
#     Data.Income_total_2011,
#     Data.Income_total_2016,
#     Data.Income_per_2006_2011,
#     Data.Income_per_2011_2016,
#     Data.Income_per_2006_2016,
#     Data.Bachelor_2006,
#     Data.Bachelor_2011,
#     Data.Bachelor_2016,
#     Data.Bachelor_per_2006_2011,
#     Data.Bachelor_per_2011_2016,
#     Data.Bachelor_per_2006_2016,
#     Data.Sum2006_2011,
#     Data.Sum2011_2016,
#     Data.Sum2006_2016
#     ]

#     session = Session(engine)
#     print("-----------------------")

#     print(session)
#     # results = session.query(*crash).filter(Data.YEAR == year).all()
#     results = session.query(*Gentrification).all()
#     session.close()

#     json_data = []
#     json_list = {}
#     for i in results:
#             json_list = {}
#             json_list["id"] = i[0]
#             json_list["SA2_Code"] = i[1]
#             json_list["SA2_Name"] = i[2]
#             json_list["Rent_2006"] = i[3]
#             json_list["Rent_2011"] = i[4]
#             json_list["Rent_2016"] = i[5]
#             json_list["Rent_per_2006_2011"] = i[6]
#             json_list["Rent_per_2011_2016"] = i[7]
#             json_list["Rent_per_2006_2016"] = i[8]
#             json_list["House_avg2006"] = i[9]
#             json_list["House_avg2011"] = i[10]
#             json_list["House_avg2016"] = i[11]
#             json_list["House_per_2006_2011"] = i[12]
#             json_list["House_per_2011_2016"] = i[13]
#             json_list["House_per_2006_2016"] = i[14]
#             json_list["Income_total_2006"] = i[15]
#             json_list["Income_total_2011"] = i[16]
#             json_list["Income_total_2016"] = i[17]
#             json_list["Income_per_2006_2011"] = i[18]
#             json_list["Income_per_2011_2016"] = i[19]
#             json_list["Income_per_2006_2016"] = i[20]
#             json_list["Bachelor_2006"] = i[21]
#             json_list["Bachelor_2011"] = i[22]
#             json_list["Bachelor_2016"] = i[23]
#             json_list["Bachelor_per_2006_2011"] = i[24]
#             json_list["Bachelor_per_2011_2016"] = i[25]
#             json_list["Bachelor_per_2006_2016"] = i[26]
#             json_list["Sum2006_2011"] = i[27]
#             json_list["Sum2011_2016"] = i[28]
#             json_list["Sum2006_2016"] = i[29]
#             json_data.append(json_list)
                
            

#     json_list_data_copy = json_list.copy()
#     json_data.append(json_list_data_copy)
#     return jsonify(json_data)




if __name__ == "__main__":
    app.run()
