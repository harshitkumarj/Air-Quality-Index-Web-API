import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'t':7.40, 'tmax':9.80, 'tmin':4.80, 'slp':1017.60, 'h':93.00, 'vv':0.50, 'v':4.30, 'vm':9.40})

print(r.json())