from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == "GET":
        print("GET")
        return render_template('mainPage.html', message="GET")
    else:
        print("POST")

    return render_template('resultPage.html', RESULT=)


if __name__ == "__main__":
    app.run(debug=True)