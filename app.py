# -*- coding: utf-8 -*-
"""app

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F5q5-fd1za80BHzdDmxRsbbjPBouP7Dr
"""

import pickle,requests,sklearn
from flask import Flask

app=Flask(__name__)
CarDekhoPrediction=pickle.load(open('CarDekhoPrediction.pkl','rb'))

from flask import render_template,request

@app.route('/',methods=['GET'])
def home():
  return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
  if(request.methods=='POST'):
    Present_Price=float(request.form['Present_Price'])
    Kms_Driven=request.form['Kms_Driven'];
    Owner=request.form['Owner']
    Number_of_years=int(2020-request.form['Year'])
    Fuel_Type=request.form['Fuel_Type_Petrol']
    if(Fuel_Type=='Petrol'):
      Fuel_Type_Diesel=0
      Fuel_Type_Petrol=1
    elif(Fuel_Type=='Diesel'):
      Fuel_Type_Diesel=1
      Fuel_Type_Petrol=0
    else:
      Fuel_Type_Diesel=0
      Fuel_Type_Petrol=0

    Seller_Type=request.form['Seller_Type_Individual']

    if(Seller_Type_Individual=='Dealer'):
      Seller_Type_Individual=0
    else:
      Seller_Type_Individual=1

    Transmission=request.form['Transmission_Mannual']

    if(Transmission=='Mannual'):
      Transmission_Manual=1
    else:
      Transmission_Manual=0

    prediction=CarDekhoPrediction.predict([[Present_Price,Kms_Driven,Owner,
        Number_of_years,Fuel_Type_Diesel,Fuel_Type_Petrol,
        Seller_Type_Individual,Transmission_Manual]])
    
    if(prediction>0):
      return render_template('index.html',prediction_text="Selling Price: {}".format(prediction))
    else:
      return render_template('index.html',prediction_text="Cant Sell")

  else:
    return render_template('index.html')

if(__name__=="__main__"):
  app.run(debug=True)
