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



		windSpeed3pm = float(request.form.get('windspeed3pm', False))
		minTemp = float(request.form.get('mintemp',False))
		humidity9am = float(request.form.get('humidity9am', False))
		pressure9am = float(request.form.get('pressure9am', False))
		windGustSpeed = float(request.form.get('windgustspeed', False))
		humidity3pm = float(request.form.get('humidity3pm', False))
		pressure3pm = float(request.form.get('pressure3pm', False))
		windSpeed9am = float(request.form.get('windspeed9am', False))
		temp3pm = float(request.form.get('temp3pm', False))
		winddDir3pm = float(request.form.get('winddir3pm', False))
		maxTemp = float(request.form.get('maxtemp', False))
		rainfall = float(request.form.get('rainfall', False))
		winddDir9am = float(request.form.get('winddir9am', False))
		month = float(request.form.get('month', False))
		day = float(request.form.get('day', False))


		input_lst = [[2, minTemp, maxTemp, rainfall,0.6,0.0,13, windGustSpeed, winddDir9am,winddDir3pm ,
					  windSpeed9am, windSpeed3pm, humidity9am, humidity3pm,
					  pressure9am, pressure3pm,8.0,0.0,16.9, temp3pm,0]]
		pred = model.predict(input_lst)
		output = pred
		if output == 0:
			return render_template("no.html")
		else:
			return render_template("yes.html")
	return render_template("index.html")

if __name__=='__main__':
	app.run(debug=True)






