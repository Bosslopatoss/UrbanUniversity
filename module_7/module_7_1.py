from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = r'C:\AlGORITM\Python_3_12_6\programms\Urban\module_7\module_7_1_folder\products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                pprint(file.read())
        except FileNotFoundError:
            print(f"Файл {self.__file_name} не найден.")
            
    def add(self, *products):
        existing_products = set()
        
        
        try:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    existing_products.add(line.strip())
        except FileNotFoundError:
            print(f"Файл {self.__file_name} не найден. Создаем новый файл.")
        print (existing_products)
        for product in products:
            if product in existing_products:
                print(f'Продукт {product.name} уже есть в магазине.')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')
                existing_products.add(product)
        print (existing_products)
                
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())