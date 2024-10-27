def custom_write(file_name, strings):
    string_positions = {}
    with open(file_name, "a", encoding="utf-8") as file:
        k = 1
        for i in strings:
            tuple_ = (k, file.tell())
            file.write(i + '\n')
            k += 1
            string_positions.update({tuple_: i})
        return string_positions 
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)