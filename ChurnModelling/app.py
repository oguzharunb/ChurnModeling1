import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('classfmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])

def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)

    print(float_features)
    print(features)    
    print(prediction)    

    return render_template('home.html', predition_text = f"Müşteri Kurumdan Ayrılacak mı? : {prediction}")

if __name__ == '__main__':
    app.run(debug= True)