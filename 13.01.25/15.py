for a in range(1000):
    if all((x <= 19) or (y <= 2 * x + a - 50) or (y > 17) for x in range(101) for y in range(101)):
        print(a)
        break
