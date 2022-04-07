import math
def valueMatrix(Matrix):

    newMatrix = []

    for i in range(len(Matrix)):
        
        row = []
        
        for j in range(len(Matrix[0])):

            row.append(Matrix[i][j])

        newMatrix.append(row)

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

def swapRows(M, indexA, indexB):

    aux = M[indexA]
    M[indexA] = M[indexB]
    M[indexB] = aux

def parcialPivoting(Ab, k, n):

    higher = math.fabs(Ab[k][k])
    higherRow = k

    for i in range(k + 1, n):

        if math.fabs(Ab[i][k]) > higher:

            higher = Ab[i][k]
            higherRow = i

    if higher == 0:

        print("The system has no unique solution.")

    elif higherRow != k:

        swapRows(Ab, k, higherRow)

    return higherRow

def backwardSubstitution(Ab):

    x = []

    for pivotIndex in range((len(Ab) - 1), -1, -1):

        summation = i =  0

        for column in range((len(Ab[0]) - 2), pivotIndex, -1):

            summation +=  Ab[pivotIndex][column] * x[i]

            i += 1

        x.append( ( Ab[pivotIndex][len(Ab[0]) - 1] - summation ) / Ab[pivotIndex][pivotIndex] )

    return x[::-1]

def gaussianPartialPivoting(AbParam, n, printStages):

    stages = [] 
    previousStages = []
    higherRowList = []

    Ab = valueMatrix(AbParam)

    # Elimination

    for k in range(n - 1):

        previousStages.append(valueMatrix(Ab))
        higherRow = parcialPivoting(Ab, k, n)
        higherRowList.append(higherRow)
        stages.append(valueMatrix(Ab))
                
        for i in range(k + 1, n):
        
            multipliers = Ab[i][k] / Ab[k][k]

            for j in range(k, n + 1):
            
                Ab[i][j] = Ab[i][j] - ( multipliers * Ab[k][j] )


    previousStages.append(valueMatrix(Ab))
    stages.append(valueMatrix(Ab))
    if printStages == True:
        for i in range (len(stages)):
            print("Stage",i,":")
            printMatrix(stages[i])
            print(" ")
    #backward substitution
    x = backwardSubstitution(Ab)
    return [stages, x, higherRowList, previousStages]

def main():
    A = [
        [2, -1, 0, 3],
        [1, 0.5, 3, 8],
        [0, 13, -2, 11],
        [14, 5, -2, 3]
    ]
    b = [1, 1, 1, 1]
    Ab = augmentedMatrix(A, b)
    
    print("Matrix A: ")
    printMatrix(A)
    print("Vector b: ")
    printMatrix(b)
    print("Matrix Ab: ")
    printMatrix(Ab)
    printStages = True
    print("after applying Gaussian substitution with partial pivoting: ")
    result = gaussianPartialPivoting(Ab, len(Ab), printStages)
    x = result[1]
    printMatrix(x)


if __name__ == "__main__":
    main()
