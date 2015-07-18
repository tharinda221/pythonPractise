__author__ = 'Ehelepola'

n1=input()
a1=input().split(" ")
List1 = list(map(int, a1))

n2=input()
a2=input().split(" ")
List2 = list(map(int, a2))

set1=set(List1);
set2=set(List2);

union=set1.union(set2)
intercept=set1.intersection(set2)

ans=union-intercept
ans=sorted(ans)
for i in range(0,len(ans)):
    print(ans[i])