#Incremental search algorithm
import math
from py_expression_eval import Parser
parser = Parser()
roots = []

def busquedasIncrementales(f, x, Delta, maxIterations):

    table = []

    fx = parser.parse(f).evaluate({"x": x})

    table.append([x, fx])

    if fx == 0:

        message = [str(x) + " is a root.", True]

    else:
        
        xNew = x + Delta
        fxNew = parser.parse(f).evaluate({"x": xNew})
       
        table.append([xNew, fxNew])
        
        Count = 1

        while fx * fxNew > 0 and Count < maxIterations:
 
            x = xNew
            fx = fxNew

            xNew = x + Delta
            fxNew = parser.parse(f).evaluate({"x": xNew})
 
            table.append([xNew, fxNew])

            Count += 1

        if fxNew == 0: 
            
            message = [str(xNew) + " is a root.", True]
        
        elif fx * fxNew < 0: 
            
            message = ["There is a root between " + str(x) + " and " + str(xNew), True] #
            roots.append([message[0]])
            busquedasIncrementales(f, xNew, Delta, (maxIterations-Count))
        
        else: 
            
            message = ["Failure in " + str(maxIterations), False]


def main():
    x0 = -3
    Deltax = 0.5
    N = 100
    f = 'log(sin(x)**2+1) - 1/2'

    busquedasIncrementales(f, x0, Deltax, N)
    for fila in roots:
        print(fila)
if __name__ == "__main__":
    main()
