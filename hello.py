from flask import Flask,request
from requests import itemRequest
app = Flask(__name__)

httpMethods = ['POST', 'GET', 'PUT', 'DELETE']


@app.route('/')
def index():
    return "app is running"

@app.route('/items',methods = httpMethods)
def items():
    var = itemRequest.getItems(request.method)
    return var


if __name__ == "__main__":
    app.run(debug=True)

