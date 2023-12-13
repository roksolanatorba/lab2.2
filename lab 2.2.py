from math import 

def sumFunc(x, h):
    sum = 0.0
    absolute_error = 0.001
    while True:
        n += 1
        term = (x**2 - 1) / math.factorial(2*n - 1)
        sum += term
        print(sum)
        if abs(term) < absolute_error:
            break
    return sum

def mathFunction(start, end, step, x, h):
    while start < end:
        value = 1.0 + sumFunc(x, start)
        start += step
    print(value)
        

a = 0
b = 0.2
h = 0.02

print("Result:")
mathFunction(a, b, h, x, h)