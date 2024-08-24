n = int(input())
result = ''
for i in range(1, n):
    for j in range(i+1, n):
        divider = i + j
        if n % divider == 0:
            result = result + str(i) + str(j)
print(result)


