m_i = int(input())
m = list(map(int, input().split()))[:m_i]
n_i = int(input())
n = list(map(int, input().split()))[:n_i]
q = [0] * 101
for i in n:
	q[i] += 1
for i in range(m_i):
	if q[i + 1] > m[i]:
		print('yes')
	else:
		print('no')