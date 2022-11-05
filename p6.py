def quadratic(a, b, c, j):
    value=0
    minx=0
    if a>=0:
        value=10000000000
        minx=10000000000
    point=-25
    while point<25:
        q=a*point**2+b*point+c
        if a>=0:
            if value>q:
                minx=point
            value=min(value, q)
        else:
            if value<q:
                minx=point
            value=max(value, q)
        point+=j
    return [round(minx, 4), round(value, 4)]

a=float(input())
b=float(input())
c=float(input())
j=float(input())

print(*quadratic(a, b, c, j))
