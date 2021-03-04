

inputfile = open("input.txt", "r")

n = int(inputfile.readline())

list_c = (inputfile.readline()).split()
list_c = [int(list_[i]) for i in range(n)]

k = int(inputfile.readline())

list_p = (inputfile.readline()).split()
list_p = [int(list_[i]) for i in range(k)]

print(k, n, "\n", list_c, "\n",list_p)
inputfile.close()


