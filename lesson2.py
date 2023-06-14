# while for  циклы
# = присваевает / == проверяет
# while True:
#     color = input('Введите цвет:')
#
#     if color == 'red':
#         print("СТОЙ")
#     elif color == "green":
#         print('Едь!!!!')
#     elif color == 'orange' or color =='yellow':
#         print('ПРИГОТОВТЕСЬ')
#     else:
#         print("Ne pravilno vveden color ")
#         break
# while 1:
#     print('apple')
# o = "*"
# while len(o) != 7:
#     o = o + "*"
#     print(o)
#
# N = int(input('Vvedite chislo'))
# for i in range(N + 1):
#     print(*(j for j in range(i + 1, N + 1)))
# # List dict tuple
# num = [2, 3, 4, 5, 6, 7, 8, 9, 0]
# pip = ['pop', 34, 23.4, True, False]
# num.append(11)  # добавляет в самый конец
# num.insert(0, 23)  # добавляет по индексу
# print(num)
# pip.remove(34)  # удаляет значение
# del pip[-1]  # удаляет по индексу

# parents = {
#     'Ira': {
#         'Piter': {
#             'dina': 'ham',
#             'gwen': "robert",
#             'mailz': "Sobaka"
#         },
#         'Parker': {
#             'suzan': {
#                 'Inna': 'Cat'
#             }
#         }
#     }
# }
# parents.update(dict(Oly="Dima"))
#
# print(parents)
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = []
# for i in a:
#     c = i * i
#     b.append(c)
# print(a)
# print(b)
#
# num = [1,3,43,543,54,32,45,0,233,4,32,43,54,53]
# even = []
# odd = []
# for i in num:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)
import random

count = 0
tries = int(input('Enter tries: '))

while count != tries:
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    product = a * b
    try:
        answer = int(input(f'{a} * {b} =?'))
        count += 1
        if answer != product:
            print(f'Nepravilno!!! Product - {product}')
        else:
            print(f'Pravilno!!!! Product - {product}')

        if tries != count:
            print(f'Tries :{tries-count}')
    except ValueError:
        print('Just only number')

print('Game Over')