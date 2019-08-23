"""function to make prediction onthe iris data set"""
import numpy as np
import pickle
from flask import jsonify
my_model = pickle.load(open('iris_model.pkl', 'rb'))
def predict_iris(data):
    #transform/parse
    predict_request = [data['SepalLengthCm'], data['SepalWidthCm'], data['PetalLengthCm'], data['PetalWidthCm']]
    predict_request = np.array(predict_request).reshape(1,-1)
    #preds
    y_hat = my_model.predict(predict_request)
    #Send back to browser
    output = {'y_hat' : int(y_hat[0])}

    return jsonify(results=output)