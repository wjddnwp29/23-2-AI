#1929 소수 구하기
M, N = map(int,input().split())

for i in range(M,N+1):
    if i == 1:
        continue
    for j in range(2,int(i**0.5)+1):
        if (i) % j == 0:
            break
    else:
        print(i)

#에라토스테네스 채의 개념을 알고있어야한다.


