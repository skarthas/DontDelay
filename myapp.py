from flask import Flask, render_template, request, redirect,json,jsonify
import requests
from bokeh.plotting import figure,show,ColumnDataSource
from bokeh.embed import components
from bokeh.resources import INLINE
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import os

myapp = Flask(__name__)

myapp.vars={}

@myapp.route('/')
def main():
  return redirect('/index')

@myapp.route('/index',methods=['Get'])
def indexes():
    
        result = None
        mystring = "Your Flight Information"

        return render_template('index3.html')
  
@myapp.route('/FindDelay')
def FindDelay():
    flnum = request.args.get('flnum');
    flac = request.args.get('flac');
    prediction = 8.136;
    return jsonify(result = 'The Flight Number you entered was ' + flac + flnum, prediction = "We predict %.2f minutes delay for this flight" %prediction);
    
  

@myapp.route('/getMyJson')
def getMyJson():
    dataFrame = pd.read_csv("{{ url_for('static', filename='unique_carrier.csv') }}")
    json = dataFrame.to_json(orient='records', date_format='iso')
    response = Response(response=json, status=200, mimetype="application/json")
    return(response)

  
if __name__ == '__main__':
  myapp.run(host='159.203.106.125',port=5000,debug=True)
