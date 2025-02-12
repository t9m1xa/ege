#f = open('c:/Users/t9m1x/Downloads/24 (6).txt').readline()
f = 'AWWDSDWWDSADWWSADDASWWSAD'
s = f.split('WW')
print(s)
m = 0 
for i in range(len(s)-3):
    s1 = 'WW'.join(s[i:i+4])
    if len(s1) > m :
        m = len(s1)
        c = s1
print(m,c)