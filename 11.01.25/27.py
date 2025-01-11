from math import dist

def centr(cl):
    r = []
    for p in cl:
        r += [(sum(dist(p, i) for i in cl), p)]
    
    return min(r)[1]

df = [tuple(map(float, s.split())) for s in open('11.01.25/27a.txt')]
cls = []
e = 1

while len(df) > 0:
    cls.append([df.pop()])
    for p in cls[-1]:
        n = [i for i in df if dist(p, i) < e]
        cls[-1] += n
        for i in n: df.remove(i)

cn = [centr(cl) for cl in cls]

px = sum(c[0] for c in cn) / len(cn)
py = sum(c[1] for c in cn) / len(cn)

print(int(px * 100), int(py * 100))