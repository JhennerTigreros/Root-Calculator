from py_expression_eval import Parser

parser = Parser()

def sec(function, puntos):
    global parser
    expr = parser.parse(function).simplify({})
    x = puntos[0]
    xAnt = puntos[1]
    errorActual = 1
    errorEsperado = (0.5 * pow(10, -6) * 100)
    iteraciones = 0
    limite = 1000

    while True:
        fx = expr.evaluate({'x': x})
        fxa = expr.evaluate({'x': xAnt})

        if (fxa - fx) == 0:
            print("División por cero")
            break

        xNew = x - ((fx * (xAnt - x)) / (fxa - fx))

        errorActual = abs((xNew - x) / xNew) * 100

        xAnt = x
        x = xNew

        iteraciones = iteraciones + 1

        if not ((errorActual > errorEsperado) and (iteraciones < limite)):
            break

    print("X: %s \nError: %s \nValor: %s" %
          (x, errorActual, expr.evaluate({'x': x})))

def fake(function, puntos):
    global parser
    expr = parser.parse(function).simplify({})
    x_l = puntos[0]
    x_u = puntos[1]
    errorActual = 1
    errorEsperado = (0.5 * pow(10, -8) * 100)
    x_r_anterior = 0
    iteraciones = 0

    print(errorEsperado)

    while True:
        valor_x_l = expr.evaluate({'x': x_l})
        valor_x_u = expr.evaluate({'x': x_u})

        x_r = x_u - (valor_x_l * (x_l - x_u)) / (valor_x_l - valor_x_u)

        valor_x_r = expr.evaluate({'x': x_r})

        if valor_x_r < 0:
            if valor_x_l < 0:
                x_l = x_r
            else:
                x_u = x_r
        else:
            if valor_x_u > 0:
                x_u = x_r
            else:
                x_l = x_r

        if iteraciones > 0:
            errorActual = abs((x_r - x_r_anterior) / x_r) * 100

        iteraciones = iteraciones + 1

        x_r_anterior = x_r

        if not(errorActual > errorEsperado):
            break

    print("X: %s \nError: %s \nValor: %s \nIteraciones %s" %
          (x_r_anterior, errorActual, expr.evaluate({'x': x_r_anterior}), iteraciones))

def fake_mod(function, puntos):
    global parser
    expr = parser.parse(function).simplify({})
def newton(function, punto):
    global parser
    expr = parser.parse(function).simplify({})

def bisection(function, punto):
    global parser
    expr = parser.parse(function).simplify({})

f = input()
fake(f, [0.5, 1.5])
