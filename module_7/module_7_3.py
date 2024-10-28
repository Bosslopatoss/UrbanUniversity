class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        punctuation_marks = (',', '.', '=', '!', '?', ';', ':', ' - ')
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                for mark in punctuation_marks:
                    content = content.replace(mark, '')
                words = content.split()
                all_words[file_name] = words
        return all_words
                
    def find(self, word):
        results = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            results[file_name] = words.index(word.lower()) + 1
        return results

    def count(self, word):
        results = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            results[file_name] = words.count(word.lower())
        return results

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего