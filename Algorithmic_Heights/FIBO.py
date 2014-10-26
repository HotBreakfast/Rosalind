#Python 2.7.5
def FibonacciNumbers(n):
    f=[0]*(n+1)
    f[1] =1
    for i in range(2,n+1):
        f[i] = f[i-1]+f[i-2]

    return f[n]


n = int(raw_input("Positivive integer n: "))
print "F%s: " %(n), FibonacciNumbers(n)
