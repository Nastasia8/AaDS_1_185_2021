a = ['Bass', 'Roach', 'Catfish', 'Trout', 'Mackerel',  'Anchovy']
b = ['Clematis', 'Dahlia', 'Rose', 'Chrysanthemum', 'Freesia', 'Lily', 'Peony']
c = ['tiger',  'leopard', 'elephant', 'camel', 'fox', 'wolf', 'raccoon']


def long(arr, simvol):
    max_item = -1
    sp = []
    for item in arr:
        if len(item) > max_item:
            max_item = len(item)
    for i in range(len(arr)):
        if len(arr[i]) != max_item:
            sp = list(arr[i])
            for j in range(max_item-len(arr[i])):
                sp.append(simvol)
            arr[i] = ''.join(sp)
            sp.clear()
    return arr


print(long(a, '$'))
