n = int(input())
list_result = []
result = ''
for i in range(1, n):
    for j in range(1, n):
        divider = i + j
        if n % divider == 0 and i != j:
            list_result.append(str(i)+str(j))
for i in list_result:
    for j in list_result:
        reversed_j = j[::-1]
        if i == reversed_j:
            list_result.remove(j)
for i in list_result:
    result = result + i
print(result)