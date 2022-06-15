import numpy as np


def dominoes(l1, l2):
    for i in range(3, n+1):
        theChoice = max(abs(l1[-i+1]-l2[-i+1])+abs(l1[-i]-l2[-i]), abs(l1[-i+1]-l1[-i])+abs(l2[-i]-l2[-i+1]))
        if abs(l1[-i]-l2[-i]) + memo[-i+1] >= theChoice + memo[-i+2]:
            memo[-i] = abs(l1[-i]-l2[-i]) + memo[-i+1]
        else:
            memo[-i] = theChoice + memo[-i+2]
    return


n = int(input())
l1 = list(map(int, input().rstrip().split()))
l2 = list(map(int, input().rstrip().split()))
memo = np.zeros(n)
memo[-1] = abs(l1[-1]-l2[-1])
memo[-2] = max(abs(l1[-1]-l2[-1])+abs(l1[-2]-l2[-2]), abs(l1[-1]-l1[-2])+abs(l2[-2]-l2[-1]))
dominoes(l1, l2)
print(memo[0])
