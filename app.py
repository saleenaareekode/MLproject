# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:30:23 2020

@author: Dell
"""

import numpy as np
from flask import Flask, request, jsonify, render_template## render_template redirect to the home page in index.html
import pickle


app = Flask(__name__) ## to initialize the flask

model = pickle.load(open('model.pkl', 'rb'))

# define from where the user inout is getting
@app.route('/')
def home():
    return render_template('index.html')

# the user input is fed to the model.py to get the predicted value and return the result
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
   
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    # display the result in same html page
    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))



if __name__ == "__main__":
    app.run(debug=True)