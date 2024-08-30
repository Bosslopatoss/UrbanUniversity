values_list = [False, 67, "abrakadabra"]
values_list_2 = [3.1415926535897932384626433832795, 'NO']
values_dict = {'a': 12, 'b': 'apple', 'c': False}
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()                          #Фунция с параметрами по умолчанию
print_params(c = [1,2,3])
print_params(b = 25)                    #Распаковка параметров
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 445)       #Распаковка + отдельные параметры
