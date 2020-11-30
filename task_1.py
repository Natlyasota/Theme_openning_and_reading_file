from pprint import pprint
import os

file_path = os.path.join(os.getcwd(), 'recipes.txt')
with open(file_path) as f:
    cook_book = {}
    name_of_specific_dish = f.readline()

    while name_of_specific_dish:
        count_of_ingredient = int(f.readline())
        final_variant_dish_description = []
        dict_of_all_ingredients_of_one_dish = {}

        for i in range(count_of_ingredient):
            name_count_measure_of_one_ingredient = f.readline().split('|')
            name = name_count_measure_of_one_ingredient[0]
            quantity = name_count_measure_of_one_ingredient[1].strip()
            measure = name_count_measure_of_one_ingredient[2].strip()

            dct_name_quantity_measure = {'ingredient_name': name, 'quantity': quantity, 'measure': measure}
            final_variant_dish_description.append(dct_name_quantity_measure)
            dict_of_all_ingredients_of_one_dish[name_of_specific_dish.strip()] = final_variant_dish_description
            cook_book.update(dict_of_all_ingredients_of_one_dish)

        f.readline()
        name_of_specific_dish = f.readline()
pprint(cook_book)


# ΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩ
# My variant with detailed comments:

# file_path = os.path.join(os.getcwd(), 'recipes.txt')
# with open(file_path) as f:
#     cook_book = {}  # создаем переменную-слварь для окончательного результата всей задачи
#     name_of_specific_dish = f.readline()  # задаем питону читать первую строку. Тут у нас имя файла
#
#     while name_of_specific_dish:  # ставим условие: пока у нас в цикле while есть переменная, которая будет носить
#         # название 'name_of_specific_dish', а таких по ходу задачи будет 4 шт.(4 названия блюда), мы
#         # делаем следующие действия:
#         count_of_ingredient = int(f.readline())  # сдвигаемся на строчку ниже и делаем из нее integer
#         final_variant_dish_description = []  # пример {'ingredient_name': 'Яйцо ', 'measure': 'шт', 'quantity': '2'}
#         dict_of_all_ingredients_of_one_dish = {}  # будет ключ name_of_specific_dish, а значением будет см.↑
#
#         for i in range(count_of_ingredient):  # итерируемся по кл-ву ингредиентов
#             name_count_measure_of_one_ingredient = f.readline().split('|')  # сдвигаемся еще на одну строчку ниже
#             name = name_count_measure_of_one_ingredient[0]
#             quantity = name_count_measure_of_one_ingredient[1].strip()
#             measure = name_count_measure_of_one_ingredient[2].strip()
#
#             dct_name_quantity_measure = {'ingredient_name': name, 'quantity': quantity, 'measure': measure}  # это
#             # временный служебный словарь, чтобы его потом добавлять в final_variant_dish_description, а тот
#             # в свою очередь добавлять в качестве value в dict_of_all_ingredients_of_one_dish
#             final_variant_dish_description.append(dct_name_quantity_measure)
#             dict_of_all_ingredients_of_one_dish[name_of_specific_dish.strip()] = final_variant_dish_description
#             cook_book.update(dict_of_all_ingredients_of_one_dish)
#
#         #  когда все итерации в range(count_of_ingredient) закончились,
#         f.readline()  # мы сдвигаемся еще на одну строчку ниже, так как у нас она пустая, ее тоже нужно пройти
#         name_of_specific_dish = f.readline()  # затем сдвигаемся еще на строчку ниже и уже в
#         # качестве name_of_specific_dish задаем текущую строчку
# pprint(cook_book)



