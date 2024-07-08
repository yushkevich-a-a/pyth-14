my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def printList(i):
    if i <= 0:
        return i
    print(my_list[printList(i - 1)])
    if i == len(my_list):
        print('Конец списка')
    return i


printList(len(my_list))