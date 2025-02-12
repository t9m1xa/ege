f = open('C:/Users/t9m1x/Downloads/24 (2).txt').readline()

f = f.replace('PP','P P')
f = f.replace('PP','P P')

s = f.split()
print(max(len(x) for x in s))