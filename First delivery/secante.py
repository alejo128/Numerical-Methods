import math 
from py_expression_eval import Parser

parser = Parser()

def secante(x, xNew, Tol, maxIterations, f):

    table = []

    fx = parser.parse(f).evaluate({"x": x})

    if fx == 0:

        message = [str(x) + " is a root.", True]     

    else:

        fxNew = parser.parse(f).evaluate({"x": xNew})

        Count = 0
        error = Tol + 1

        denominador = fxNew - fx

        table.append([Count, x, fx, 0])
        table.append([Count + 1, xNew, fxNew, 0])

        while error > Tol and fxNew != 0 and denominador != 0 and Count < maxIterations:

            xAuxiliar = xNew - fxNew * (xNew - x) / denominador

            error = abs(xAuxiliar - xNew)

            x = xNew
            fx = fxNew

            xNew = xAuxiliar
            fxNew = parser.parse(f).evaluate({"x": xNew})

            denominador = fxNew - fx

            Count += 1

            table.append([Count + 1, xNew, fxNew, error])

        if fxNew == 0: 

            message = [str(xNew) + " is a root.", True]     

        elif error < Tol: 

            message = [str(xNew) + " is an approximation to a root with tol=" + str(Tol), True]     

        elif denominador == 0: 

            message = ["there is a possible multiple root", True]     

        else: 

            message = ["Failure in " + str(maxIterations) + " iterations.", False]

    return [table, message]

def main():
    a = secante(0.5,1,0.0000001,100,"log(sin(x)**2 + 1) - 1/2")
    print('\n')
    print(a)

if __name__ == "__main__":
    main()

