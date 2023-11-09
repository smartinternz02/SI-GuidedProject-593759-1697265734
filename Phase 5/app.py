# -*- coding: utf-8 -*-
from flask import Flask,render_template,url_for,request,jsonify
from flask_cors import cross_origin
import pandas as pd
import numpy as np
import datetime
import pickle

app = Flask(__name__, template_folder="template")
model = pickle.load(open("rain.pkl", "rb"))
print("Model Loaded")

@app.route("/",methods=['GET'])
@cross_origin()
def home():
	return render_template("index.html")

@app.route("/predict",methods=['GET', 'POST'])
@cross_origin()
def predict():
	if request.method == "POST":
		# DATE

		# MinTemp
		minTemp = float(request.form.get['mintemp',False])
		# MaxTemp
		maxTemp = float(request.form.get['maxtemp',False])
		# Rainfall
		rainfall = float(request.form.get['rainfall',False])
		# Evaporation
		evaporation = float(request.form.get['evaporation',False])
		# Sunshine
		sunshine = float(request.form.get['sunshine',False])
		# Wind Gust Speed
		windGustSpeed = float(request.form.get['windgustspeed',False])
		# Wind Speed 9am
		windSpeed9am = float(request.form.get['windspeed9am',False])
		# Wind Speed 3pm
		windSpeed3pm = float(request.form.get['windspeed3pm',False])
		# Humidity 9am
		humidity9am = float(request.form.get['humidity9am',False])
		# Humidity 3pm
		humidity3pm = float(request.form.get['humidity3pm',False])
		# Pressure 9am
		pressure9am = float(request.form.get['pressure9am',False])
		# Pressure 3pm
		pressure3pm = float(request.form.get['pressure3pm',False])
		# Temperature 9am
		temp9am = float(request.form.get['temp9am',False])
		# Temperature 3pm
		temp3pm = float(request.form.get['temp3pm',False])
		# Cloud 9am
		cloud9am = float(request.form.get['cloud9am',False])
		# Cloud 3pm
		cloud3pm = float(request.form.get['cloud3pm',False])
		# Cloud 3pm
		location = float(request.form.get['location',False])
		# Wind Dir 9am
		winddDir9am = float(request.form.get['winddir9am',False])
		# Wind Dir 3pm
		winddDir3pm = float(request.form.get['winddir3pm',False])
		# Wind Gust Dir
		windGustDir = float(request.form.get['windgustdir',False])
		# Rain Today
		rainToday = float(request.form.get['raintoday',False])

		input_lst = [location , minTemp , maxTemp , rainfall , evaporation , sunshine ,
					 windGustDir , windGustSpeed , winddDir9am , winddDir3pm , windSpeed9am , windSpeed3pm ,
					 humidity9am , humidity3pm , pressure9am , pressure3pm , cloud9am , cloud3pm , temp9am , temp3pm ,
					 rainToday , month , day]
		pred = model.predict(input_lst)
		output = pred
		if output == 0:
			return render_template("after_sunny.html")
		else:
			return render_template("after_rainy.html")
	return render_template("predictor.html")

if __name__=='__main__':
	app.run(debug=True)






