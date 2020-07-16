def fibonacci(n):
    if n == 0:
        global count_0
        count_0 = count_0 +1
        return 0
    elif n == 1:
        global count_1
        count_1 = count_1 + 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

arr = []
num = int(input())
for i in range (num):
    n = int(input())
    count_0 = 0
    count_1 = 0
    fibonacci(n)
    arr.append(str(count_0) + ' ' + str(count_1))
for i in arr:
    print(i)