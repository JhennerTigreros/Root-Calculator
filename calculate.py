from flask import Flask, url_for, request, render_template, redirect
import logging

app = Flask(__name__)
app.secret_key = "jhenner123"

@app.route("/main", methods=["POST", "GET"])
def main():
    return render_template("calculate.html")


@app.route("/calculate/root/newton-raphson", methods=["POST"])
def calculate_newton():
    if request.method == "POST":
        function = request.form["function"]
        puntos = [request.form["punto_1"], request.form["punto_2"]]
        print("Función : %s, Punto : %s" % (function, puntos))
    return "Hola"

@app.route("/calculate/root/fake-position", methods=["POST"])
def calculate_fake_position():
    if request.method == "POST":
        function = request.form["function"]
        puntos = [request.form["punto_1"], request.form["punto_2"]]
        print("Función : %s, Punto : %s" % (function, puntos))
    return "Fake position"

@app.route("/calculate/root/sec", methods=["POST"])
def calculate_sec():
    if request.method == "POST":
        function = request.form["function"]
        puntos = [request.form["punto_1"], request.form["punto_2"]]
        print("Función : %s, Punto : %s" % (function, puntos))
    return "Secante"

@app.route("/calculate/root/bisection", methods=["POST"])
def calcualte_bisection():
    if request.method == "POST":
        function = request.form["function"]
        puntos = [request.form["punto_1"], request.form["punto_2"]]
        print("Función : %s, Punto : %s" % (function, puntos))
    return "Bisection"

@app.route("/calculate/root/fake-position-mod", methods=["POST"])
def calculate_fake_position_mod():
    if request.method == "POST":
        function = request.form["function"]
        puntos = [request.form["punto_1"], request.form["punto_2"]]
        print("Función : %s, Punto : %s" % (function, puntos))
    return "Fake position mod"

app.run(debug=True)
