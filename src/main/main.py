from flask import Flask
from flask import render_template
from flask import request
import os

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
        data = [
  {'name': "Monte Falco", 'height': 1658, 'place': "Parco Foreste Casentinesi" },
  {'name': "Monte Falterona", 'height': 1654, 'place': "Parco Foreste Casentinesi" },
  {'name': "Poggio Scali", 'height': 1520, 'place': "Parco Foreste Casentinesi" },
  {'name': "Pratomagno", 'height': 1592, 'place': "Parco Foreste Casentinesi" },
  {'name': "Monte Amiata", 'height': 1738, 'place': "Siena" }]
    return render_template('resultPage.html', data_dict=data)


if __name__ == "__main__":
    app.run(debug=True)