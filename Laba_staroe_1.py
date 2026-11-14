def list_comparison(list_1, list_2):
    return list_1[0] == list_2[0] or list_1[-1] == list_2[-1]

print(list_comparison([1, 2, 3], [1, 5, 6, 7, 8])) # Первые равны
print(list_comparison([1, 2, 3, 4], [4, 5, 3])) # Последние равны
print(list_comparison([1, 2, 3], [4, 5, 6, 7])) # Ничего не равно
print(list_comparison([1, 2], [1, 2, 3])) # Все совпадает
print(list_comparison([7], [7])) # Списки из 1 элемента