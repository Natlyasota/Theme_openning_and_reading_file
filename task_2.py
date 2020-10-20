from pprint import pprint

with open(r'/Users/USER/Desktop/Open and reading file/py-homework-basic-files/2.4.files/recipes.txt') as f:
    cook_book = {} # создаем переменную-слварь для окончательного результата всей задачи
    row = f.readline() # создаем переменную для построчного чтения
    while row != '': # ставим условие выполнения задачи до тех пор, пока построчное чтение не закончится

        count_of_ingr_in_recept = int(f.readline()) # переменная показывает, сколько ингредиентов должно быть в одном рецепте. Тут мы как бы говорим питону - возьми и пройдись по каждой строке и найди а ней строку, в которой есть число и сделай эту строку числом
        dict_of_all_ingr_of_one_dish = {} # создаем пустой словарь для каждого рецепта блюда с полным описанием
        final_variant_dish_description = [] # здесь полное описание каждого ингредиента по типу {'ingredient_name': 'Яйцо ', 'measure': 'шт', 'quantity': '2'}

        for i in range(count_of_ingr_in_recept): # а раз count_of_ingr_in_recept у нас в данном случае включает цифры 3, 4, 3, 5 это значит, что сначала мы питерируемся в диапазоне 3, потом 4, потом 3, потом 5
            a = f.readline().split('|') # говорим, чтобы питон 'расщипил' наш текст запятыми на месте символа '|'

            name_of_ingredient = a[0] # далее задаем 3 переменные, которые требуются в условии задачи
            quantity = a[1].strip() # здесь .strip() в основном нужен, чтобы \n убрать, которые нам .readline() автоматически ставит
            measure = a[2].strip() # то же самое

            final_variant_of_line = {'ingredient_name': name_of_ingredient, 'quantity': quantity, 'measure': measure}
            final_variant_dish_description.append(final_variant_of_line) # добавляем в пустой словарь полное описание рецепта блюда

            dict_of_all_ingr_of_one_dish[row.strip()] = final_variant_dish_description # самый важный момент кода: у словаря первого уровня вложенности создаем ключи и значения. .strip() ставится для избежания \n. В качеслве ключа мы ставим row
            cook_book.update(dict_of_all_ingr_of_one_dish)

        f.readline() # задаем 'шаг' для считывания файла
        row = f.readline() # прописываем и внутри цикла while, чем у нас будет являться row
# pprint(cook_book) # ГЛАВНАЯ ПРОВЕРКА ВСЕГО КОДА

#         pprint(count_of_ingr_in_recept) # проверяем count_of_ingr_in_recept
#         pprint(dict_of_all_ingr_of_one_dish) # проверяем dict_of_all_ingr_of_one_dish
#         pprint(final_variant_dish_description) # проверяем final_variant_dish_description



def get_shop_list_by_dishes(dishes, person_count=0):
    for key, value in cook_book.items():
        for s in value:
            s['quantity'] = int(s.get('quantity')) * person_count
        if key in dishes:
            pprint(value)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

