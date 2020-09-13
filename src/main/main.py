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

        data = [{'x':'trump', 'value':10, 'date':100, 'sentiment':50},
                {'x':'brump', 'value':6, 'date':2, 'sentiment':30},
                {'x':'arump', 'value':4, 'date':17, 'sentiment':20},
                {'x':'trump', 'value':1, 'date':10, 'sentiment':500}]

    return render_template('resultPage.html', data_dict=json.dumps(data))


if __name__ == "__main__":
    app.run(debug=True)