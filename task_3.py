from pprint import pprint
import os # импортируем для создания платформо-независимых путей

file_path_1 = os.path.join(os.getcwd(), '/Users/USER/Desktop/Open and reading file/py-homework-basic-files/2.4.files/sorted/1.txt')
with open(file_path_1) as f_1:
    file_name_1 = '1.txt' # это нужно только для дальнейшего вывода информации в формате название - длительность
    dct_1 = {} # словарь, в котором будет контент файла '1.txt' и кол-во строк. Это словарь именно для этого файла. Он нужен, чтобы мы могли сравнивать размеры каждого файла (в зависимости от кол-ва строк) благодаря величине значения
    counter_1 = [] # сюда добавляем текст из файла. Можно было прибегнуть к .readlines(), но мне так неудобно
    for i in f_1: # итерируемся для построчного добавления контента файла и список. Опять же, можно было прибегнуть к .readlines(), но мне так неудобно
        counter_1.append(i.strip()) # .strip() помогает избавиться от \n и других пробелоа, переносов строки и тд.
        ln_1 = len(counter_1) # теперь создаем переменную для длины файла, ниже она нам везде пригодится
    dct_1[tuple(counter_1)] = ln_1 # вот и заполняем dct_1, который был пустым. Пишу tuple, так как без него питон не дает работать. Тут ключ у нас название, значение - длина
# pprint(dct_1)

file_path_2 = os.path.join(os.getcwd(), '/Users/USER/Desktop/Open and reading file/py-homework-basic-files/2.4.files/sorted/2.txt')
with open(file_path_2) as f_2:
    file_name_2 = '2.txt'
    dct_2 = {}
    counter_2 = []
    for i in f_2:
        counter_2.append(i.strip())
        ln_2 = len(counter_2)
    dct_2[tuple(counter_2)] = ln_2
# pprint(dct_2)

file_path_3 = os.path.join(os.getcwd(), '/Users/USER/Desktop/Open and reading file/py-homework-basic-files/2.4.files/sorted/3.txt')
with open(file_path_3) as f_3:
    file_name_3 = '3.txt'
    dct_3 = {}
    counter_3 = []
    for i in f_3:
        counter_3.append(i.strip())
        ln_3 = len(counter_3)
    dct_3[tuple(counter_3)] = ln_3
# pprint(dct_3)


dc = {} # создаем словарь словарей для того, чтобы его сортировать по ключам
dc.update(dct_1)
dc.update(dct_2)
dc.update(dct_3)
# pprint(dc)
a = sorted(dc.items(), key=lambda x: x[1]) # это я нагуглил. Хорошая формула для сортировки словаря по значениям. Важно!!! Этот трюк возвращает уже не словарь, а список.
# pprint(a)


# на время отрываемся и переходим к блоку про название - длительность
filename_list = [file_name_1, file_name_2, file_name_3]
len_list = [ln_1, ln_2, ln_3]
z = zip(filename_list, len_list) # зипуем названия с длительностями
ee = list(z)


# делаем все то же самое, что для сортировки файлов, но теперь для блока "название - длительность"
cc = {}
for i in ee:
    cc[i[0]] = i[1] # превращаем зипованный список название - длительность в словарь, где название - ключ, длительность - значение
# print(cc)
vv = sorted(cc.items(), key=lambda x: x[1]) # ту же нагугленную формулу используем для сортирвки по значениям
# print(vv)
for i in vv: # 1-й вывод информации
    print(i)


# теперь нам нужно вывести информацию красиво, без скобок, запятых и тп.
d = []
for i in a: # см стр. 43
    d.append(list(i[0])) # если так оставить, то все 3 файла будут идти как одинк списко с 3 вложенными списками
d[0].extend(d[1]) # Поэтому мы делаем так, что первый вложенный список поглащает второй, а затем и третий. И в итоге остается единый список без вложений
d[0].extend(d[2])
k = (d[0]) # просто, чтобы лучше читалось
for i in k: # 2-й вывод информации
    print(i)












