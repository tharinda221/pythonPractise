__author__ = 'Ehelepola'


n=int(input())

T=input().split(" ")
tuple=int(T[0]),int(T[1])
for i in range(2,n):
    tuple=tuple+ (int(T[i]),)

#print(tuple)
print(hash(tuple))
