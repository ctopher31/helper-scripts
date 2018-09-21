# Fibonacci numbers module

#
# Write Fibonacci series up to n
#
# param1: the number to write the sequence up to
#
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        result.append(a)
        a, b = b, a + b
    print()
    return result

if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))
