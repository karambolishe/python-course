# -*- encoding: utf-8 -*-
d = {0: 0, 1: 0, 2: 0}

for a in range(0,4):
    if d.has_key(a):
        d[a] += 1
    else:
        d[a] = d.setdefault(a,0)

print(d)

