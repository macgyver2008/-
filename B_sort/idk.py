import random
A = []
for a in range(5):
    A.append(random.randrange(1, 50))



def bubble_sort() :
    for i in range(len(A)):
        for k in range(1, len(A)):
            if A[k-1] > A[k]:
                A[k], A[k-1] = A[k-1], A[k]
    return A
import random
A = []
backUp = 0
for a in range(5):
    A.append(random.randrange(1, 50))
# print(A)
# A = bubbleSort(A)
# print(A)

def select_sort(A):
    s = A[0]
    for k in range(len(A)):
        s = k
        for i in range(k, len(A)):
            print(s)
            if A[s] > A[i]:
                s = i
        A[k], A[s] = A[s], A[k]


L = select_sort(A)
print(L)



def insert_sort(A):

    for i in range(1, len(A)):
        k = i - 1
        key = A[i]
        while A[k] > key and k >= 0:
            A[k-1] = A[k]
            k = k-1
        A[k+1] = key
    return A

B = insert_sort(A)
print(B)











n = int(input())
A =[]
for i in range(n):
    A.append(int(input()))
def bubble_sort() :
    for i in range(n-1):
        for k in range(n - i -1):
            if A[k-1] > A[k]:
                A[k], A[k-1] = A[k-1], A[k]
    return A


for i in bubble_sort():
    print(i)

