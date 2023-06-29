import csv
from flask import Flask, render_template, request, redirect, url_for
import diseaseprediction
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    p = request.form['Symptom1']
    q = request.form['Symptom2']
    r = request.form['Symptom3']
    s = request.form['Symptom4']
    t = request.form['Symptom5']
    pre = [[int(p), int(q), int(r), int(s), int(t)]]
    output = model.predict(pre)
    return render_template('index.html', prediction_text='Disease can be $ {}'.format(output[0]))

if __name__ == '__main__':
    app.run(debug=True)
