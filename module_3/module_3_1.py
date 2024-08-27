calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string_):
    count_calls()
    len_string_ = len(string_)
    UP_string_ = string_.upper()
    LOW_string_ = string_.lower()
    tuple_ = (len_string_, UP_string_, LOW_string_)
    return tuple_
def is_contains(string_, list_to_search):
    count_calls()
    string_ = string_.lower()
    list_to_search = [i.lower() for i in list_to_search]
    if string_ in list_to_search:
        return True
    else:
        return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)


