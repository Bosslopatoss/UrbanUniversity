numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True                         #переменная флаг
for i in numbers: 
    if i == 1:
        continue                      
    for j in range(2, i):               #проверка на простоту числа 
        if i % j == 0:
            is_prime = False
            break 
        else:
            is_prime = True
    if is_prime == True:                #добавление чисел в списки
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)
