for n in range(1,100):
    s=bin(n)[2:]
    s=s[::-1]
    s=s+s[-1]
    r=int(s,2)
    if r>99:
        print(n)
        break
