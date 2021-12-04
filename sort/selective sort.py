import random
'''
선택형 정열 (selective sort)
'''
a = []
for l in range(5):
    a.append(random.randrange(1, 50))


s = a[0]
for k in range(len(a)) :
    s = k
    for i in range(k, len(a)):
        if a[s] > a[i] :
            s = i
    a[k],a[s] = a[s],a[k]
print(a)
