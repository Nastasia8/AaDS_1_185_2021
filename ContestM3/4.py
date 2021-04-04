
def pre_count(substring):
    count  = 1
    p = [0]*len(substring)
    for i in range(len(substring)-1):
        j = p[i]
        while j > 0 and substring[j] != substring[i+1]:
            j = p[j-1]
        if substring[j] == substring[i+1]:
            p[i+1] = j+1
        else:
            p[i+1] = 0
        if p[i+1] < 2:
            count = i+1
    return count 

def main():
    substring = input()
    print(pre_count(substring))

main()