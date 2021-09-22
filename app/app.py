import numpy as np
from flask import Flask, request, jsonify, render_template
from build_model.py import value

# initialize a new Flask app
app = Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return "You visited the %s page" % (path)
#open the model
#loaded_model = pickle.load(open('modelsmall.pkl', 'rb'))

#home page
@app.route('/')
def home():
    return render_template('home.html')
@app.route("/acknowledgements.html")
def acknowledgements():
    return render_template("acknowledgements.html")
# predict page after Submit
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    # post method to get and send data back
    if request.method == 'POST':
            #update chars
            name = str(request.form['name'])
            spot = str(request.form['spot'])
            speed = float(request.form['speed'])
            bright = float(request.form['bright'])
            describe = str(request.form['describe'])
            # got rid of predict
            message = build_model.value(name, spot, speed, bright, describe)
        # run errror check
    return render_template('predict.html', prediction = message)
if __name__ == "__main__":
    app.run()
