import math

def Frog(nR, nC, arr):
    J = []
    for i in range(nR):
        temp = []
        for j in range(nC):
            temp.append(math.inf)
        J.append(temp)
    J[0][0] = 0
    
    for i in range(nR):
        for j in range(nC):
            k = 1
            while k<=arr[i][j][0] and k+j<nC:
                J[i][j+k] = min(J[i][j+k],1+J[i][j])
                k += 1
            k = 1
            while k<=arr[i][j][1] and k+i<nR:
                J[i+k][j] = min(J[i+k][j],1+J[i][j])
                k += 1
    #print(J)
    print(J[nR-1][nC-1])
    
if __name__ == '__main__':
    n = list(map(int, input().rstrip().split()))
    #print(n)
    arr = []
    R = []
    D = []
    for i in range(n[0]):
        R.append(list(map(int, input().rstrip().split())))

    for i in range(n[0]):
        D.append(list(map(int, input().rstrip().split())))
    for i in range(n[0]):
        temp = []
        for j in range(n[1]):
            temp.append([R[i][j],D[i][j]])
        arr.append(temp)  

    Frog(n[0],  n[1], arr)
