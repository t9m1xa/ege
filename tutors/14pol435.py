for x in range(19):
    n1=9*19**7+8*19**6+x*19**5+7*19**4+9*19**3+6*19**2+4*19+1
    n2=3*19**4+6*19**3+x*19**2+1*19+4
    n3=7*19**3+3*19**2+x*19+4
    n=n1+n2+n3
    if n%18==0:
        print(n//18)
