def mathematicalFunction(n,X):
    commonRatio = (1 / X)
    firstNumber = (1/X)
    sumTillNthTerm = (firstNumber * (1 - commonRatio**n)) / (1 - commonRatio)
    return sumTillNthTerm

print(mathematicalFunction(5,4))