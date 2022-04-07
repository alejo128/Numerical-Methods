import math

def valueMatrix(Matrix):

    newMatrix = []

    for i in range(len(Matrix)):
        
        fila = []
        
        for j in range(len(Matrix[0])):

            fila.append(Matrix[i][j])

        newMatrix.append(fila)

    return newMatrix

def augmentedMatrix(A, b):

    augmentedMatrix = []

    Acopy = valueMatrix(A)

    for i in range(len(Acopy)):
    
        Acopy[i].append(b[i])

        augmentedMatrix.append(Acopy[i])

    return augmentedMatrix

def printMatrix(Matrix): 
    for row in Matrix: print(row)

def backwardSubstitution(Ab):

    x = []

    for pivotIndex in range((len(Ab) - 1), -1, -1):

        sum = i =  0

        for column in range((len(Ab[0]) - 2), pivotIndex, -1):

            sum +=  Ab[pivotIndex][column] * x[i]

            i += 1

        x.append( ( Ab[pivotIndex][len(Ab[0]) - 1] - sum ) / Ab[pivotIndex][pivotIndex] )

    return x[::-1]

def swapRows(M, indexA, indexB):

    aux = M[indexA]
    M[indexA] = M[indexB]
    M[indexB] = aux

def swapColumns(M, indexA, indexB, mark):

    auxMark = mark[indexA]
    mark[indexA] = mark[indexB]
    mark[indexB] = auxMark

    for i in range(len(M)):

        aux = M[i][indexA]
        M[i][indexA] = M[i][indexB]
        M[i][indexB] = aux


def totalPivoting(Ab, k, n, mark):
 
    higher = 0

    higherRow = k
    higherColumn = k

    for i in range(k, n):
        for j in range(k, n):

            if math.fabs(Ab[i][j]) > higher:

                higher = math.fabs(Ab[i][j])
                higherRow = i
                higherColumn = j

    if higher == 0:

        print("The system has no unique solution.")

    else:

        if higherRow != k: 

            swapRows(Ab, k, higherRow)

        if higherColumn != k:

            swapColumns(Ab, k, higherColumn, mark)

    return [higherRow, higherColumn]



def gaussianTotalPivoting(AbParam, n, printStages):

    stages = [] 
    previousStages = []
    higherList = []
    
    mark = []

    for i in range(n): mark.append(i)

    Ab = valueMatrix(AbParam)

    # Eliminación

    for k in range(n - 1):

        previousStages.append(valueMatrix(Ab))

        higherIndex = totalPivoting(Ab, k, n, mark)
        
        higherRow = higherIndex[0]
        higherColumn = higherIndex[1]

        higherList.append([higherRow, higherColumn])
        stages.append(valueMatrix(Ab))
        
        for i in range(k + 1, n):
        
            multiplicator = Ab[i][k] / Ab[k][k]

            for j in range(k, n + 1):
            
                Ab[i][j] = Ab[i][j] - ( multiplicator * Ab[k][j] )

    previousStages.append(valueMatrix(Ab))
    stages.append(valueMatrix(Ab))
    if printStages == True:
        for i in range (len(stages)):
            print("stages",i,":")
            printMatrix(stages[i])
            print(" ")
    # backward substitution
    x = backwardSubstitution(Ab)

    return [stages, x, higherList, previousStages, mark]

def main():
    """A = [
        [2, -1, 0, 3],
        [1, 0.5, 3, 8],
        [0, 13, -2, 11],
        [14, 5, -2, 3]
    ]
    b = [1, 1, 1, 1]"""
    A = [
        [4,2,1],
        [0.25,0.5,1],
        [1,1,0]
    ]
    b = [1,0,0]
    Ab = augmentedMatrix(A, b)
    
    print("Matrix A: ")
    printMatrix(A)
    print("Vector b: ")
    printMatrix(b)
    print("Matrix Ab: ")
    printMatrix(Ab)
    printStages = True
    print("*******************************************************************************")
    print("After applying Gaussian substitution with total pivoting: ")
    result = gaussianTotalPivoting(Ab, len(Ab), printStages)
    print("results x: ")
    x = result[1]
    printMatrix(x)

if __name__ == "__main__":
    main()