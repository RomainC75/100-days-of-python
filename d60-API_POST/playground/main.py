from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=['GET'])
def get():
    return render_template('index.html', )


@app.route("/", methods=['POST'])
def post_data():
    print("data", request.form)
    name=request.form['name']
    password=request.form['password']
    
    return "<h1>Data received</h1>"


app.run(debug=True)