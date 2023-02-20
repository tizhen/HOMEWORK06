# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

# import NumPy as np
 
# a = np.random.randint(0, 9, 20)  # диапазон случайных чисел
# b = range(1, 7) # заданный диапазон
# m = 5 # заданный максимум
# i = [i for i,j in enumerate(a) if (j in b) and (j<m)]
# d = np.delete(a, i)
 
# print('Исходный диапазон:', a)
# print('Индексы:', i)
# print('Новый диапазон:', a[i])
# print('Преобразованный исходный диапазон:', d)


from random import randint
 
lo, hi = 3, 8
data = [randint(1, 10) for _ in range(20)]
print("Исходный диапазон:", data, sep='\n')
indexes = [i for i, v in enumerate(data) if lo <= v <= hi]
print("Индексы: ", indexes, sep='\n')
result = []
i = len(indexes)
while i :
    i -= 1
    result.append(data.pop(indexes[i]))
print("Новый диапазон: ", data, sep='\n')
print("Преобразованный диапазон: ", result, sep='\n')