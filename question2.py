def nextNumber(requiredElement):
    firstElement = 2
    firstDifference = 1
    secondDifference = 7
    iteratorDifference = 4
    if requiredElement == 1:
        return firstElement
    else:
        currentElement = firstElement
        for i in range(2,requiredElement+1):
            if i % 2 == 0:
                currentElement = currentElement + firstDifference
                firstDifference = firstDifference + iteratorDifference
            else:
                currentElement = currentElement + secondDifference
                secondDifference = secondDifference + iteratorDifference
        return currentElement
