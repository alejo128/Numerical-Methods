import math 
from py_expression_eval import Parser

parser = Parser()

def newton(x, Tol, maxIterations, f, df):

    table = []
    
    fx = parser.parse(f).evaluate({"x": x})
    
    derive = parser.parse(df).evaluate({"x": x})

    Count = 0
    error = Tol + 1

    table.append([Count, x, fx, derive, 0]) 

    while error > Tol and Count < maxIterations and fx != 0 and derive != 0:

        xNew = x - (fx / derive)
    
        fx = parser.parse(f).evaluate({"x": xNew})
        
        derive = parser.parse(df).evaluate({"x": xNew})

        error = abs(xNew - x)

        x = xNew

        Count += 1

        table.append([Count, x, fx, derive, error]) 

    if fx == 0: 

        message = [str(x) + " is a Root.", True] 

    elif error <= Tol: 

        message = [str(x) + " is an approximation with Tol " + str(Tol), True] 

    elif derive == 0: 

        message = [str(xNew) + "is a possible square root", True] 

    else: 

        message = ["Failure in " + str(maxIterations) + " iterations.", False]

    return [table, message]

def main():
    a = newton(0.55, 0.00001, 100, "(0.44*(x**2))-(0.44*x)+0.11", "0.88*x-0.44")
    print('\n')
    for row in a[0]:
        print(row)
    print(a[1])

if __name__ == "__main__":
    main()

