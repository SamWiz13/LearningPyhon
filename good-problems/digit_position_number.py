n = int(input("n = "))
s = 0
k = 1
i = 0
while i < n:
	d = k
	m = 0
	while d > 0:
		d //= 10
		m += 1
	for t in range(m - 1,-1,-1):
		s = k // 10 ** t % 10
		i += 1
		if i == n:
			break
	k += 1
print(s)
a = ""
for i in range(1, n+1):
	a += str(i)
print(a[n - 1])