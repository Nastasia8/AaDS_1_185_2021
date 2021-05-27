colvo=int(input())#ввод количества
spisok=[]#создаем список
for i in range(colvo):#цикл
	spisok.append(input().split())#добавляем элементы в список 
spisok=[[int(spisok[i][j]) for j in range(2)]for i in range(colvo)]
for i in range(colvo-1):# цикл без последнего 
	for j in range(colvo-i-1):# цикл до и-1
		if spisok[j][1]<spisok[j+1][1]:# если меньше, то меняем местами
			spisok[j],spisok[j+1]=spisok[j+1],spisok[j]
		if spisok[j][1]==spisok[j+1][1]:
			if spisok[j][0]>spisok[j+1][0]:# если больше, то меняем местами
				spisok[j],spisok[j+1]=spisok[j+1],spisok[j]
[print(i[0],i[1]) for i in spisok]#выводим значения из списка