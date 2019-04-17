from flask import Flask, url_for, request, render_template, redirect
import logging
from utils import *

app = Flask(__name__)
app.secret_key = "jhenner123"

@app.route("/", methods=["POST", "GET"])
@app.route("/main", methods=["POST", "GET"])
def main():
    return render_template("calculate.html")


@app.route("/calculate/root/newton-raphson", methods=["POST"])
def calculate_newton():
    if request.method == "POST":
        function = request.form["function"]
        puntos = [float(request.form["punto_1"]), float(request.form["punto_2"])]
    return ' '.join(newton(function, puntos))

@app.route("/calculate/root/fake-position", methods=["POST"])
def calculate_fake_position():
    if request.method == "POST":
        function = request.form["function"]
        puntos = [float(request.form["punto_1"]), float(request.form["punto_2"])]
    return ' '.join(fake(function, puntos))

@app.route("/calculate/root/sec", methods=["POST"])
def calculate_sec():
    if request.method == "POST":
        function = request.form["function"]
        puntos = [float(request.form["punto_1"]), float(request.form["punto_2"])]
    return ' '.join(sec(function, puntos))

@app.route("/calculate/root/bisection", methods=["POST"])
def calcualte_bisection():
    if request.method == "POST":
        function = request.form["function"]
        puntos = [float(request.form["punto_1"]), float(request.form["punto_2"])]
    return ' '.join(bisection(function, puntos))

@app.route("/calculate/root/fake-position-mod", methods=["POST"])
def calculate_fake_position_mod():
    if request.method == "POST":
        function = request.form["function"]
        puntos = [float(request.form["punto_1"]), float(request.form["punto_2"])]
    return ' '.join(fake_mod(function, puntos))

app.run(debug=True)
