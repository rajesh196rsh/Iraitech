def mathematicalFunction(n,X):
    if n == 1:
        return 1/X
    else:
        return (1 / X**n) + mathematicalFunction(n-1,X)

print(mathematicalFunction(5,4))