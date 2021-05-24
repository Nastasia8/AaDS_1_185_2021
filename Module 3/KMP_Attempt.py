def FindPi(form):
    p = [0] * len(form)
    i = 1; j = 0
    while i < len(form):
        if form[j] == form[i]:
            p[i] += j + 1
            i += 1; j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j - 1]
    return(p)

def KMPAlgorithm(string, form):
    FindPi(form)
    m = len(form); n = len(string)
    i = j = 0
    while i < n:
        if string[i] == form[j]:
            i += 1; j += 1
            if j == m:
                print("Образ найден")
                break
            else:
                if j > 0:
                    j = p[j - 1]
                else:
                    i += 1
    if i == n:
        print("Образ не найден")
    
def main():
    string = input("Введите строку: ")
    form = input("Введите образ для поиска по строке: ")
    KMPAlgorithm(string, form)

main()