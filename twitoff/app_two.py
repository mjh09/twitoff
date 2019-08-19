from flask import Flask, render_template # instance of class
app = Flask(__name__) # creat instance of flask

@app.route('/') # web page (endpoint)
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000) # debug mode, specified port
