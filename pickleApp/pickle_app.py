import numpy as np
from flask import Flask, jsonify, request
import pickle
from predict_iris import predict_iris

#model
my_model = pickle.load(open('iris_model.pkl', 'rb'))
X = pickle.load(open('iris_x_test.pkl', 'rb'))
y = pickle.load(open('iris_y_test.pkl', 'rb'))


app = Flask(__name__)

@app.route('/api', methods=['POST'])
def make_predict():
    #get data
    data = request.get_json(force=True)
    output = predict_iris(data)
    return output


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