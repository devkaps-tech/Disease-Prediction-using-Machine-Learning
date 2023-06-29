
from flask import Flask, render_template, request
import numpy as np
import pickle

#import mySQLdb

app = Flask(__name__)
#conn = MySQLdb.connect(host='localhost',user='root',password='',db='disease_database')
model = pickle.load(open(r'C:/Users/Lenovo/Desktop/ezyZip/Disease Prediction system using Machine Learning/model.pkl' , 'rb'))

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/login', methods=['POST'])
def login() : 
    p = request.form['S1']
    q = request.form['S2']
    r = request.form['S3']
    s = request.form['S4']
    t = request.form['S5']
    u = request.form['S6']
    v = request.form['S7']
    w = request.form['S8']
    x = request.form['S9']
    y = request.form['S10']
    
   
    pre = [[int(p) , int(q) , int(r) , int(s) , int(t) , int(u),int(v),int(w),int(x),int(y)]]
    output = model.predict(pre)
    return render_template('index.html', y ='Disease can be {}'.format(str(output[0])))

# @app.route('/default')
# def default():
#         return render_template('includes/default.html')
 

if __name__ == '__main__':
    app.run(debug=False)