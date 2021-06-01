# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:12:42 2020

@author: Dell
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())