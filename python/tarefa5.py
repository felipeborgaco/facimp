def fact(x, dict):
    if x in dict:
        return dict[x]
    if x == 1:
        dict[x] = 1
        return 1
    dict[x] = x*fact(x-1, dict)
    return dict[x]


def fibo(x, dict):
    if x in dict:
        return dict[x]
    if x == 0 or x == 1:
        dict[x] = x
        return x
    dict[x] = fibo(x-1, dict) + fibo(x-2, dict)
    return dict[x]


x = int(input("digite um numero: "))

dict = {}

print(fibo(x, dict))
