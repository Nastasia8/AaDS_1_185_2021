number = list(range(1,20))
y=input()
z=input()
[number**y**z if number%2==1 else number for number in range(1,21)]
print(number)