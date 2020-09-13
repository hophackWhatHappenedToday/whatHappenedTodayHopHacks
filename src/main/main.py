from flask import Flask
from flask import render_template
from flask import request
import os

template_dir = os.path.abspath('../../templates')
app = Flask(__name__, template_folder=template_dir, static_folder='../../static')


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == "GET":
        print("GET")
        return render_template('mainPage.html', message="GET")
    else:
        print("POST")
        source = request.form.getlist('newssource')
        sort = request.form['sort']
        time = request.form['time']
        range = request.form['rangeInput']
        categories = request.form.getlist('categories')
        print(source)
        print(sort)
        print(time)
        print(range)
        print(categories)
        data = filter(source, sort, time, range, categories)
    return render_template('resultPage.html', data_dict=data)


if __name__ == "__main__":
    app.run(debug=True)