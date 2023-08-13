# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def check_variables_add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))


@app.route('/sub')
def check_variables_sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a, b))

@app.route('/mult')
def check_variables_mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a, b))

@app.route('/div')
def check_variables_div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a, b))

operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<operation>')
def preform_operation(operation):
    if operation in operations:
        a = int(request.args["a"])
        b = int(request.args["b"])
        result = operations[operation](a,b)
        return str(result)
    else:
        return "Invalid operation"