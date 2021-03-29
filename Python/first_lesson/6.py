text = "Hello hi how hello are and you I am fine thank you and you hello You Thank And"
arr = text.split()
arr_2 = []
sl = {}
for item in arr:
    arr_2.append(item.lower())
print(arr_2)
for item in arr_2:
    if item in sl:
        sl[item] += 1
    else:
        sl[item] = 1
print(sl)
