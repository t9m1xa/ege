for i in range ( 1000 , 9999+1):
   c = sorted([int(x) for x in str(i)])
   if len(set(c)) == 4:
      a = str(min(c) + max(c))
      b = str(c[1]*c[2])
      r = int(a+b)
      if r > 85 :
         print(i)
         break


