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

    return [x, errorActual, expr.evaluate({'x': x})]

def fake(function, puntos):
    global parser
    expr = parser.parse(function).simplify({})
    
    x_l = puntos[0]
    x_u = puntos[1]
    
    errorActual = 1
    errorEsperado = (0.5 * pow(10, -8) * 100)
    
    x_r_anterior = 0
    
    iteraciones = 0

    while True:
        valor_x_l = expr.evaluate({'x': x_l})
        valor_x_u = expr.evaluate({'x': x_u})

        x_r = x_u - (valor_x_u * (x_l - x_u)) / (valor_x_l - valor_x_u)

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

    return [x_r_anterior, errorActual, expr.evaluate({'x': x_r_anterior}), iteraciones]

def fake_mod(function, puntos):
    global parser
    expr = parser.parse(function).simplify({})

    x_l = puntos[0]
    x_u = puntos[1]
    x_r = 0

    contador_x_l = 0
    contador_x_u = 0

    errorEsperado = (0.5 * pow(10, -8) * 100)
    errorActual = 1

    x_r_anterior = 0

    iteraciones = 0

    while True:
        valor_x_l = expr.evaluate({'x': x_l})
        valor_x_u = expr.evaluate({'x': x_u})

        if contador_x_u == 2 or contador_x_l == 2:
            x_r = (x_l + x_u) / 2
            contador_x_l = 0
            contador_x_u = 0
        else:
            x_r = x_u - (valor_x_u * (x_l - x_u)) / (valor_x_l - valor_x_u)

        valor_x_r = expr.evaluate({'x': x_r})

        if valor_x_r < 0:
            if valor_x_l < 0:
                x_l = x_r
                contador_x_l = contador_x_l + 1
                contador_x_u = 0
            else:
                x_u = x_r
                contador_x_u = contador_x_u + 1
                contador_x_l = 0
        else:
            if valor_x_u > 0:
                x_u = x_r
                contador_x_u = contador_x_u + 1
                contador_x_l = 0
            else:
                x_l = x_r
                contador_x_l = contador_x_l + 1
                contador_x_u = 0

        if iteraciones > 0:
            errorActual = abs((x_r - x_r_anterior) / x_r) * 100

        x_r_anterior = x_r

        iteraciones = iteraciones + 1

        if not(errorActual > errorEsperado):
            break

    return [x_r_anterior, errorActual, expr.evaluate({'x': x_r_anterior}), iteraciones]
    


def newton(function, puntos):
    global parser
    expr = parser.parse(function).simplify({})

    x = puntos[0]
    x_ant = puntos[1]

    errrorEsperado = (0.5 * pow(10, -8) * 100)
    errorActual = 1
    limite_iteraciones = 1000

    iteraciones = 0

    try:
        while True:
            y = expr.evaluate({'x': x})
            #Falata derivada
            x = x - (y / 1)
            errorActual = abs((x - x_ant) / x) * 100
            x_ant = x
            iteraciones = iteraciones + 1
            if not(errorActual>errrorEsperado and iteraciones < limite_iteraciones):
                break

        if iteraciones >= limite_iteraciones:
            return ["Se excedio de la cantidad de iteraciones.", x, errorActual, expr.evaluate({'x': x_ant}), iteraciones]
    except ZeroDivisionError:
        print("División por cero.")
        return ["División por cero.", x, errorActual, expr.evaluate({'x': x_ant}), iteraciones]


def bisection(function, puntos):
    global parser
    expr = parser.parse(function).simplify({})

    x_l = puntos[0]
    x_u = puntos[1]

    errorEsperado = (0.5 * pow(10, -8) * 100)
    errorActual = 1

    x_r_anterior = 0

    iteraciones = 0

    while True:
        x_r = (x_l + x_u) / 2

        valor_x_l = expr.evaluate({'x': x_l})
        valor_x_u = expr.evaluate({'x': x_u})
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

    return [x_r_anterior, errorActual, expr.evaluate({'x': x_r_anterior}), iteraciones]

