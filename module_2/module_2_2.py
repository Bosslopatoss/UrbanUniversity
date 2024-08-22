first = int(input())
second = int(input())
thrid = int(input())

if first == second == thrid:
    print(3)
elif first == second != thrid:
    print(2)
elif first == thrid != second:
    print(2)
elif second == thrid != first:
    print(2)
else:
    print(0)