from flask import Flask, render_template, request, redirect, url_for
import pickle
app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username']!='admin' or request.form['password']!='admin':
            error = 'Invalid credentials. Please try again!'
        else:
            return render_template('main.html')
    return render_template('layout.html',error = error)

@app.route('/logout', methods = ["GET","POST"])
def logout():
    return render_template("layout.html")

@app.route('/ad', methods = ["GET","POST"])
def account_details():
    return render_template("accd.html")

@app.route('/back', methods = ["GET","POST"])
def back():
    return render_template("main.html")

@app.route('/mod', methods = ["GET","POST"])
def Modify():
    return render_template("modify.html")

if __name__ == '__main__':
    app.run(debug=True)