from math import gcd

def buildTree(value, left, right, tree, array):
    if right - left == 1:
        tree[value] = array[left]
        return
    middle = (right + left) // 2
    buildTree(2 * value + 1, left, middle, tree, array)
    buildTree(2 * value + 2, middle, right, tree, array)
    tree[value] = gcd(tree[2 * value + 1], tree[2 * value + 2])

def getMax(value, left, right, tree, qLeft, qRight):
    if qLeft <= left and qRight >= right:
        return tree[value]
    if qLeft >= right or qRight <= left:
        return 0
    middle = (right + left) // 2
    tLeft = getMax(2 * value + 1, left, middle, tree, qLeft, qRight)
    tRight = getMax(2 * value + 2, middle, right, tree, qLeft, qRight)

    return gcd(tLeft, tRight)

def main():
    n = int(input())
    array = list(map(int, input().split(maxsplit = n)))
    tree = [0] * 4 * n
    buildTree(0, 0, n, tree, array)
    q = int(input())
    index = []
    while q !=0:
        left, right = map(int,input().split())
        index.append(getMax(0, 0, n, tree, left - 1, right))
        q -= 1
    print(*index)

main()