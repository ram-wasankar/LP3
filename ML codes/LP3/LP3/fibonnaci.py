#DAA exp1: Write a program non-recursive and recursive program to calculate Fibonacci numbers
#and analyze their time and space complexity.		
#In this code step count it calculated but not given in problem statement of our ICEM DAA index



def fibonacci_iter(n):
    if n < 0:
        return -1, 1
    if n == 0 or n == 1:
        return n, 1
    steps = 0
    a = 0
    b = 1
    print("Iterative series:", a, b, end=" ")
    for i in range(2, n + 1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
        steps += 1
    print()  # new line after series
    return c, steps  # removed +1


def fibonacci_recur(n):
    if n < 0:
        return -1, 1
    if n == 0 or n == 1:
        return n, 1
    fib1, steps1 = fibonacci_recur(n - 1)
    fib2, steps2 = fibonacci_recur(n - 2)
    return fib1 + fib2, steps1 + steps2 + 1


def print_recursive_series(n):
    print("Recursive series:", end=" ")
    for i in range(n + 1):
        print(fibonacci_recur(i)[0], end=" ")
    print()


if __name__ == '__main__':
    n = int(input("Enter a number: "))
    fib_iter, steps_iter = fibonacci_iter(n)
    print("Iterative:", fib_iter)
    print("Steps:", steps_iter)

    print_recursive_series(n)
    fib_recur, steps_recur = fibonacci_recur(n)
    print("Recursive:", fib_recur)
    print("Steps:", steps_recur)
