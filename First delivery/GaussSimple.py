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


def backwardSubstitution(Ab):

    x = []

    for pivotIndex in range((len(Ab) - 1), -1, -1):

        sum = i =  0

        for column in range((len(Ab[0]) - 2), pivotIndex, -1):

            sum +=  Ab[pivotIndex][column] * x[i]

            i += 1

        x.append( ( Ab[pivotIndex][len(Ab[0]) - 1] - sum ) / Ab[pivotIndex][pivotIndex] )

    return x[::-1]


def simpleGaussian(AbParam, n, printstages):

    #AbParam is the augmented Matrix Ab
    #n = len(AbParam)
    stages = [] 
    
    Ab = valueMatrix(AbParam)

    stages.append(valueMatrix(Ab))
  
    # elimination

    for k in range(n - 1):

        stageMultipliers = []
        
        for i in range(k + 1, n):
        
            multiplicator = Ab[i][k] / Ab[k][k]

            for j in range(k, n + 1):
            
                Ab[i][j] = Ab[i][j] - ( multiplicator * Ab[k][j] )

        stages.append(valueMatrix(Ab))

    if printstages == True:
        for i in range (len(stages)):
            print("stage",i,":")
            printMatrix(stages[i])
            print(" ")

    #backward substitution:
    x = backwardSubstitution(Ab)
    return[x]
    
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
    printstages = True
    print("After applying simple Gaussian substitution: ")
    result = simpleGaussian(Ab, len(Ab), printstages)
    print("results x: ")
    printMatrix(result)

if __name__ == "__main__":
    main()
