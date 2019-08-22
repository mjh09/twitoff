import numpy as np
from flask import Flask, jsonify, request
import pickle

#model
my_model = pickle.load(open('iris_model.pkl', 'rb'))
X = pickle.load(open('iris_x_test.pkl', 'rb'))
y = pickle.load(open('iris_y_test.pkl', 'rb'))


app = Flask(__name__)

@app.route('/api', methods=['POST'])
def make_predict():
    #get data
    data = request.get_json(force=True)
    #transform/parse
    predict_request = [data['SepalLengthCm'], data['SepalWidthCm'], data['PetalLengthCm'], data['PetalWidthCm']]
    predict_request = np.array(predict_request).reshape(1,-1)
    #preds
    y_hat = my_model.predict(predict_request)
    #Send back to browser
    output = {'y_hat' : int(y_hat[0])}
    return jsonify(results=output)


@app.route('/score', methods=['POST'])
def score():
    score = my_model.score(X,y)
    output = {'score' : '{:.2f}'.format(score)}
    return jsonify(results=output)


#@app.route('/predict/')
#@app.route('/predict/<input>', methods=['POST'])
#def predict(input=None):
#    new_in = input_to_
#    return render_template('predict.html', input=output)



if __name__ == '__main__':
    app.run(port = 5000, debug=True)