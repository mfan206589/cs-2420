def fibinacci(n):
    if n < 0:
        return 0
    a,b = 1,1
    for i in range (n-1):
        a,b = b, a + b
    return b
def fibinacciRecursive(n):
    if n == 0 or n == 1: return 1
    return fibinacciRecursive(n-1) + fibinacciRecursive(n-2)
print(fibinacci(500))
print(fibinacciRecursive(5))