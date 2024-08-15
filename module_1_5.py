immutable_var = 'apple', 3, 52, 'ie'
print(immutable_var)
# Если мы попытаемся изменить элементы кортежа, экран выведет ошибку, т.к. тип Tuple является неизменяемым.
mutable_list = ['ou ea', 228, True, 'urban']
mutable_list.append(616)
mutable_list.extend('NO')
mutable_list.remove(228)
print(mutable_list)
