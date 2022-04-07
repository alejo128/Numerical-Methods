import math
from py_expression_eval import Parser

parser = Parser()

def raicesMultiples(x, Tol, maxIterations, f, df, ddf):

    table = []

    fx = parser.parse(f).evaluate({"x": x})
    fdx = parser.parse(df).evaluate({"x": x})
    fddx = parser.parse(ddf).evaluate({"x": x})
    
    Count = 0
    error = Tol + 1
    
    table.append([Count, x, fx, fdx, fddx, 0])

    while error > Tol and Count < maxIterations and fx != 0 and fdx != 0:
       
        xNew = x - ((fx * fdx) / (math.pow(fdx, 2) - fx * fddx)) 
        
        fx = parser.parse(f).evaluate({"x": xNew})
        fdx = parser.parse(df).evaluate({"x": xNew})
        fddx = parser.parse(ddf).evaluate({"x": xNew})

        error = abs(xNew - x)
        
        x = xNew

        Count += 1

        table.append([Count, x, fx, fdx, fddx, error])
    
    if fx == 0: 
        
        message = [str(x) + " is a root.", True]     
    
    elif error <= Tol: 
        
        message = [str(x) + "is an approximation to a root with tol=" + str(Tol), True]     
    
    elif fdx == 0: 
        
        message = ["There's a possible multiple root", True]     
    
    else: 
        
        message = ["Failure in " + str(maxIterations) + " iterations.", False]

    return [table, message]

def main():
    hx = "exp(x)-x-1"
    dhx = "exp(x)-1"
    ddhx = "exp(x)"
    TOL = 0.0000001
    N = 100
    x0 = 1
    resultado = raicesMultiples(1, TOL, N, hx, dhx, ddhx)
    print(resultado)

if __name__ == "__main__":
    main()
