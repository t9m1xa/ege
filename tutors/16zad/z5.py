def F( n ):
  global k
  k += 1
  if n >= 1:
    k+=1
    F(n-1)
    F(n-2)
    F(n-3)
k = 0
F(22)
print(k)
