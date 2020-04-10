
def myPow(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    elif k == 2:
        return n * n
    else:
        prev = myPow(n, k // 2)
        if k % 2 == 0:
            return prev * prev % 1000000007
        else:
            return prev * prev * n  % 1000000007


n, k= map(int, input().split(' '))

print(myPow(n, k))