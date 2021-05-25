def buildTree(value, leftEdge, rightEdge, treeOfSegments, array):
    if rightEdge - leftEdge == 1:
        treeOfSegments[value] = array[leftEdge]
        return
    middle = (rightEdge + leftEdge) // 2
    buildTree(2 * value + 1, leftEdge, middle, treeOfSegments, array)
    buildTree(2 * value + 2, middle, rightEdge, treeOfSegments, array)
    treeOfSegments[value] = treeOfSegments[2 * value + 1] + treeOfSegments[2 * value + 2]

def getSum(value, leftEdge, rightEdge, treeOfSegments, qLeftEdge, qRightEdge):
    if qLeftEdge <= leftEdge and qRightEdge >= rightEdge:
        return treeOfSegments[value]
    elif qLeftEdge >= rightEdge or qRightEdge <= leftEdge:
        return 0
    else:
        middle = (rightEdge + leftEdge) // 2
        tLeftEdge = getSum(2 * value + 1, leftEdge, middle, treeOfSegments, qleftEdge, qrightEdge)
        tRightEdge = getSum(2 * value + 2, middle, rightEdge, treeOfSegments, qleftEdge, qrightEdge)
        return tLeftEdge + tRightEdge

def searchingKZeroOnASegment(value, leftEdge, rightEdge, treeOfSegments, k):
    if rightEdge - leftEdge == 1:
        return rightEdge
    if k > treeOfSegments[value]:
        return -1
    middle = (rightEdge + leftEdge) // 2
    if k <= treeOfSegments[2 * value + 1]:
        return searchingKZeroOnASegment(2 * value + 1, leftEdge, middle, treeOfSegments, k)
    else:
        return searchingKZeroOnASegment(2 * value + 2, middle, rightEdge, treeOfSegments, k - treeOfSegments[2 * value + 1])

def updatingValue(value, leftEdge, rightEdge, treeOfSegments, index, newValue):
    if rightEdge - leftEdge == 1:
        treeOfSegments[value] = newValue
        return
    middle = (leftEdge + rightEdge) // 2
    if index < middle:
        updatingValue(2 * value + 1, leftEdge, middle, treeOfSegments, index, newValue)
    else:
        updatingValue(2 * value + 2, middle, rightEdge, treeOfSegments, index, newValue)
    treeOfSegments[value] = treeOfSegments[2 * value + 1] + treeOfSegments[2 * value + 2]

def main():
    n = int(input())
    array = [0 if int(i) != 0 else 1 for i in input().split()]
    treeOfSegments = [0] * 4 * n
    buildTree(0, 0, n, treeOfSegments, array)
    numberOfRequests = int(input())
    result = []
    for _ in range(numberOfRequests):
        inputData = input().split()
        if inputData[0] == "s":
            leftEdge, rightEdge, k = int(inputData[1]), int(inputData[2]), int(inputData[3])
            sumFromASegment = getSum(0, 0, n, treeOfSegments, leftEdge - 1, rightEdge)
            if sumFromASegment >= k and leftEdge == 1:
                result.append(searchingKZeroOnASegment(0, 0, n, treeOfSegments, k))
            elif sumFromASegment >= k and leftEdge > 1:
                result.append(searchingKZeroOnASegment(0, 0, n, treeOfSegments, k + getSum(0, 0, n, treeOfSegments, 0, leftEdge - 1)))
            else:
                result.append(-1)
        else:
            index, newValue = int(inputData[1]), int(inputData[2])
            if newValue == 0:
                updatingValue(0, 0, n, treeOfSegments, index - 1, 1)
            else:
                updatingValue(0, 0, n, treeOfSegments, index - 1, 0)
    print(*result)

main()

'''
5
0 0 3 0 2
3
u 1 5
u 1 0
s 1 5 3
'''

#Ошибка во время исполнения, но пример решает верно