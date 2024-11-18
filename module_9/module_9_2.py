first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Шаг 1
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Шаг 2
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# Шаг 3
combined_strings = first_strings + second_strings
third_result = {s: len(s) for s in combined_strings if len(s) % 2 == 0}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)