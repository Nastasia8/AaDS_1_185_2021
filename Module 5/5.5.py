from math import gcd


def build(value, left, right, tree, array):
    if right - left == 1:
        tree[value] = array[left]
        return
    middle = (right + left) // 2
    build(2 * value + 1, left, middle, tree, array)
    build(2 * value + 2, middle, right, tree, array)
    tree[value] = gcd(tree[2 * value + 1], tree[2 * value + 2])

def update(value, left, right, tree, index, newValue):
    if right - left == 1:
        tree[value] = newValue
        return
    middle = (right + left) // 2
    if index < middle:
        update (2 * value + 1, left, middle, tree, index, newValue)
    else:
        update (2 * value + 2, middle, right, tree, index, newValue)
    tree[value] = gcd(tree[2 * value + 1],tree[2 * value + 2])


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
    build(0, 0, n, tree, array)
    q = int(input())
    index = []
    while q != 0:
        queue, left, right = map(str, input().split())
        if queue == "s":
            index.append(getMax(0, 0, n, tree, int(left) - 1, int(right)))
        else:
            update(0, 0, n, tree, int(left) - 1, int(right))
        q -= 1
    print(*index)


main()


'''
Штирлиц долго смотрел в одну точку. Потом в другую. "Двоеточие!" - наконец-то смекнул Штирлиц.
'''