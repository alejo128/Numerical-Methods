import math 
from py_expression_eval import Parser

parser = Parser()


def puntoFijo(x, Tol, maxIterations, f, g):

    table = [] 

    fx = parser.parse(f).evaluate({"x": x})

    Count = 0
    error = Tol + 1

    table.append([Count, x,fx, 0]) 

    while error > Tol and Count < maxIterations and fx != 0:


        xNew = parser.parse(g).evaluate({"x": x})

        fx = parser.parse(f).evaluate({"x": xNew})

        error = abs(xNew - x)

        x = xNew

        Count += 1

        table.append([Count, x, fx, error]) 

    if fx == 0: 

        message = [str(x) + " is a root.", True] 

    elif error <= Tol: 

        message = [str(x) + " is an approximation with tol " + str(Tol), True] 

    else: 

        message = ["Failure in " + str(maxIterations) + " iterations.", False] 

    return [table, message]


def main():
    a = puntoFijo(1, 0.00001, 100, "exp(x-10.5)+sin(x)+(x**3)-2*x", "exp(x-10.5)+(sin(x))+(x**3)-x")
    print('\n')
    for row in a[0]:
        print(row)
    print(a[1])

if __name__ == "__main__":
    main()
