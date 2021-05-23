def prefix(string):
    p = [0] * len(string)
    index = 1
    for i in range(len(string)-1):
        j = p[i]
        while j > 0 and string[j] != string[i + 1]:
            j = p[j - 1]
        if string[j] == string[i + 1]:
            p[i + 1] = j + 1
        else:
            p[i + 1] = 0
        if p[i + 1] < 2:
            index = i + 1
    return index


def main():
    string = str(input())
    print(prefix(string))


main()