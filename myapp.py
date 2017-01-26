from flask import Flask, render_template, request, redirect
import requests
import simplejson as json
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

@myapp.route('/index',methods=['Get','POST'])
def indexes():
  return render_template('index3.html')

  
if __name__ == '__main__':
  myapp.run(host='159.203.106.125',port=5000,debug=True)
