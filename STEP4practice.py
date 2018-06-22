n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
    
#隣接リスト
l = [[] for i in range(n)]
for pi in p:  #0-originedに注意
    l[pi[0]].append(pi[1])
    l[pi[1]].append(pi[0])
print(l)