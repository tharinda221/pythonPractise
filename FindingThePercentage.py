from collections import defaultdict

__author__ = 'Ehelepola'

n=int(input(""))
ans=0.0
x = defaultdict(list)
for i in range(0,n):
    names=input().split(" ")
    x['student'].append(names)

student=input()
for r in range(0,n):
    for j in range(0,n+1):

        if x['student'][r][j]==student :

            for k in range(1,4):
                #print(float(x['student'][r][k]))
                ans=ans+float(x['student'][r][k])


print ("{:.2f}".format(ans/3))