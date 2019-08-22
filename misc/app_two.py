from flask import Flask, render_template # instance of class

""" how to run: python app_two.py """

app = Flask(__name__) # creat instance of flask

@app.route('/') # web page (endpoint)
def home():
    return render_template('home.html') # use template

@app.route('/about') # new page from root
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000) # debug mode, specified port
