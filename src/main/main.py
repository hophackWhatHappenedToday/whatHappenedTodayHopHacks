from flask import Flask
from flask import render_template
from flask import request
import os
import json

template_dir = os.path.abspath('../../templates')
app = Flask(__name__, template_folder=template_dir, static_folder='../../static')


@app.route('/', methods=['POST', 'GET'])
def main():
    return keywordlist()


@app.route('/', methods=['POST', 'GET'])
def keywordlist():
    if request.method == "GET":
        print("GET")
        return render_template('mainPage.html', message="GET")
    else:
        print("POST")
        source = request.form.getlist('newssource')
        time = request.form['time']
        range = request.form['rangeInput']
        categories = request.form.getlist('categories')
        data = [{'id': 123, 'data': 'qwerty', 'indices': [1,10]}, {'id': 345, 'data': 'mnbvc', 'indices': [2,11]}]

    return render_template('resultPage.html', data_dict=data)


if __name__ == "__main__":
    app.run(debug=True)