my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
k = 0
while k < len(my_list):
    if my_list[k] > 0:
        print(my_list[k])
    elif my_list[k] == 0:
        k += 1
        continue
    else:
        break
    k += 1
