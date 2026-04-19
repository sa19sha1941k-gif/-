# x = 0
# sum = 0
# while x <= 5:
#     sum += x
#     x += 1
# print(sum)

# x = 0
# while x < 10:
#     x += 1
#     print(x )
# while x > 0:
#     x -= 1
#     print(x)



# for i in range(1,11):
#     print(i)

list_of_pakupachki = []
while True:
    a = input('1 - добавление элемента, 2 - удаление элемента, 3 - вывести список, 4 - закончить список ')
    if a == '1':
        list_of_pakupachki.append(input('Введите продукт, который нужно добавить '))
    elif a == '2':
        list_of_pakupachki.remove(input('Введите продукт, который нужно удалить '))
    elif a == '3':
        print(list_of_pakupachki)
    elif a == '4':
        break
for i in list_of_pakupachki:
    print(i)









