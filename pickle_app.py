import numpy as np
from flask import Flask, jsonify, request
import pickle

#model
my_model = pickle.load(open('iris_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def make_predict():
    #get data
    data = request.get_json(force=True)
    #transform/parse
    predict_request = [data['SepalLengthCm'], data['SepalWidthCm'],data['PetalLengthCm'], data['PetalwidthCm'], data[]]
    predict_request = np.array(predict_request).reshape(1,-1)
    #preds
    y_hat = my_model.predict(predict_request)
    #Send back to browser
    output = {'y_hat' : int(y_hat[0])}
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)