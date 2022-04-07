import math
from py_expression_eval import Parser

parser = Parser()

def reglaFalsa(xLower, xHigher, Tol, maxIterations, f):

    table = [] 


    fxLower = parser.parse(f).evaluate({"x": xLower})
    fxHigher = parser.parse(f).evaluate({"x": xHigher})

    if fxLower == 0:

        message = [str(xLower) + " is a Root.", True] 

    elif fxHigher == 0:

        message = [str(xHigher) + " is a Root.", True] 

    elif fxLower * fxHigher < 0:

        Count = 1

        xMedium = xLower - ((fxLower * (xHigher - xLower)) / (fxHigher - fxLower))
        fxMedium = parser.parse(f).evaluate({"x": xMedium})

        table.append([Count, xLower, xHigher, xMedium, fxMedium, 0])

        error = Tol + 1

        while error > Tol and fxMedium != 0 and Count < maxIterations:

            if fxLower * fxMedium < 0:

                xHigher = xMedium
                fxHigher = fxMedium

            else:

                xLower = xMedium
                fxLower = fxMedium

            Aux = xMedium

            xMedium = xLower - ((fxLower * (xHigher - xLower)) / (fxHigher - fxLower))
            fxMedium = parser.parse(f).evaluate({"x": xMedium})

            error = abs(xMedium - Aux)

            Count += 1

            table.append([Count, xLower, xHigher, xMedium, fxMedium, error])

        if fxMedium == 0:

            message = [str(xMedium) + " is a Root.", True]

        elif error < Tol:

            message = [str(xMedium) + " is an approximation to a root with a tolerance = " + str(Tol), True]

        else:

            message = ["Failure in " + str(maxIterations), False]

    else:

        message = ["The interval is inadequate.", False]

    return [table, message]


def main():
    a = reglaFalsa(0,1,0.0000001,100,"log(sin(x)**2 + 1) - 1/2")
    print('\n')
    print(a)

if __name__ == "__main__":
    main()
