k = 24*1.0
m = 20*1.0
n = 29*1.0
denom = (k+m+n)*(k+m+n-1)
print (k*m/denom) + (k*n/denom) + (k*(k-1)/denom) + (n*k/denom) + ((0.5)*(n*m/denom)) + ((0.5)*(m*n/denom)) + ((0.75)*(m*(m-1)/denom)) + (m*k/denom)
