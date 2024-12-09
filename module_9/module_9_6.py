def all_variants(text):
    subsequences = [text[start:end] for start in range(len(text)) for end in range(start + 1, len(text) + 1)]
    subsequences.sort(key=len)
    for subseq in subsequences:
        yield subseq

# Пример использования функции-генератора
a = all_variants("abc")
for i in a:
    print(i)