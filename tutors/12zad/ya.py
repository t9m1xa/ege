
for n in range(1,1000):
    s = n*'5'
    while '34' in s or '55' in s:
        if '34' in s:
            s = s.replace('34','54321',1)
        else:
            if '55' in s:
                 s = s.replace('55','234',1)
    
    if 1000 <= len(s) <= 9999:
        print(n)
        break
