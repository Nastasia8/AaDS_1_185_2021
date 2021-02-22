#10 из 08.02
numbers = [6, 43, -2, 11, -555, -12, 3, 345, 0]
print({number: "+" if number>0 else "-" if number<0 else "zero" for number in numbers})
