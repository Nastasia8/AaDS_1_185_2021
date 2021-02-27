a = ["Bass", "Roach", "Catfish", "Trout", "Mackerel",  "Anchovy"]
b = ["Clematis", "Dahlia", "Rose", "Chrysanthemum", "Freesia", "Lily", "Peony"]
c = ["tiger",  "leopard", "elephant", "camel", "fox", "wolf", "raccoon"]

def find_max_length(list_):
    max_ = max([len(i) for i in list_])
    return max_

def addition(list_, max_):
    for i in list_:
        if len(i) < max_:
            list_[list_.index(i)] = i + "%" * (max_ - len(i))
    return list_

print(addition(a, find_max_length(a)))
print(addition(b, find_max_length(b)))
print(addition(c, find_max_length(c)))