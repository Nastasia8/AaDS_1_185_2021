def prefixFunction(string, lenght):
    prefix = [0] * lenght
    for i in range(lenght - 1):
        j = prefix[i]
        while j > 0 and string[i + 1] != string[j]:
            j = prefix[j - 1]
        if (string[i + 1] == string[j]):
            prefix[i + 1] = j + 1
        else:
            prefix[i + 1] = 0
    return prefix

def main():
    string = input()
    lenght = len(string)
    prefix = prefixFunction(string, lenght)
    if (lenght % (lenght - prefix[-1]) == 0):
        print(lenght // (lenght - prefix[-1]))
    else:
        print(1)

main()