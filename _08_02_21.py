#2

s = []
p = []
i = 1
while i < 21:
    p.append(1)
    s.append(i**2)
    i = i + 2
print(p)
print(s, "\n")

print([n**2 for n in range(1, 21, 2)])

#3

i = int(input())
n = 1
while n < 1:
    print("\n", 2**(n + 1))
    n = n + 1

#4

s =  [7, 1, 3, 4, 3, 9, 14, -5, -17, -13, -19, -18]
r = 0
i = 0
while i < 12:
    if s[i] < 0:
        r = r + s[i]
    i = i + 1
print(r)

#5

x_list = []
for i in range(1, 21):
    x_list.append(i)
print(x_list)
y = int(input())
z = int(input())

def funct(x_list, y, z):
    i = 0
    while i < 20:
        if x_list[i] % 2 == 0:
            x_list[i] = x_list[i]**y**z
        else:
            x_list[i] = x_list[i]
        i = i + 1
    return(x_list)
print(funct(x_list, y, z))

#6

text = "Hello hi how hello are and you I am fine thank you and you hello You Thank And"
text = text.lower().split(" ")
_dict = {}
for _text in text:
    if _text in _dict:
        _dict[_text] = _dict[_text] + 1
    else:
        _dict[_text] = 1
print(_dict)

#7

matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(matrix[0])
print(matrix[1])
print(matrix[2])
i = 2
for j in range(0, 3):
    matrix[i][j] = matrix[i][j] * 2
    i = i - 1
print(matrix[0])
print(matrix[1])
print(matrix[2])