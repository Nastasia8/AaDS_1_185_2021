numbers = [7, 1, 3, 4, 3, 9, 14, -5, -17, -13, -19, -18]
sum = 0
sum1 = 0
for i in numbers:
    if i < 0:
        sum += i
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        sum1 += numbers[i]
    i += 1

print(sum)
print(sum1) 