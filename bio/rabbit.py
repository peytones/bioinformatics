
fib = {0:0,1:1}
def rab(n,k):
	if n in fib:
		return fib[n]
	else:
		f = rab(n-1,k) + rab(n-2,k)*k
		fib[n] = f
		return f

print rab(29,4)