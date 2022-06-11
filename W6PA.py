def sss(jobs):
    cnt = 0
    t = 0
    for j in jobs:
        if t<j[1]:
            cnt += 1
            t = j[0]
        else:
            continue
    print(cnt)
    return

  
n = int(input())
jobs = []
for i in range(n):
    l = list(map(int, input().rstrip().split()))
    jobs.append([l[0]+l[1]-1, l[0]])
jobs.sort()

sss(jobs)
