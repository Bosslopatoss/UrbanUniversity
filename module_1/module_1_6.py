my_dict = {'Dmitry': 175, 'Andrey': 181, 'Anastasia': 158} # 'Имя': Рост
print(my_dict)
print(my_dict['Dmitry'])
print(my_dict.get('Vasiliy'))
my_dict.update({'Saha': 193,
                'Alex': 173})
d = my_dict.pop('Andrey')
print(d)
print(my_dict)
my_set = {1, 2, 2.56, 1, 'head', 'No', 4, 0}
print(my_set)
my_set.add(9)
my_set.remove('head')
print(my_set)