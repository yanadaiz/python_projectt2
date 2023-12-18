n = int(input())
if n==0:
    print(1)
s = '1'
for i in range(n+1):
    print((n-i)*' ' + s + (n-i)*' ')
    if i==0:
        s = '1 1'
    else:
        A = list(map(int,s.split()))
        s = '1 '
        for k in range(len(A)-1):
            s = s + str(A[k]+A[k+1]) + ' '
        s = s + '1'
