# Homework 1
from pprint import pprint
with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        recipe_name = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for _ in range(ingredients_count):
            ingr = file.readline()
            name, count, units = ingr.strip().split(' | ')
            ingredient = {
                'ingredient_name': name,
                'quantity': count,
                'measure': units
            }
            ingredients.append(ingredient)
        file.readline()
        cook_book[recipe_name] = ingredients
    #pprint(cook_book, sort_dicts=False)

# Homework 2
def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for i in cook_book[dish]:
                if i['ingredient_name'] in ingredients:
                    ingredients[i['ingredient_name']].update(quantity = ingredients[i['ingredient_name']]['quantity'] + int(i['quantity']) * person_count)
                else:
                    ingredient = {
                        'measure': i['measure'],
                        'quantity': int(i['quantity']) * person_count
                    }
                    ingredients[i['ingredient_name']] = ingredient
        else:
            print(f'Блюдо "{dish}" отсутствует в cook_book')
    return ingredients

#pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2), sort_dicts=False)

# Homework 3
Files_count_line = {}
for i in range(1, 4):
    with open(f'Sorted/{i}.txt', 'rt', encoding='utf-8') as file:
        result = file.readlines()
        Files_count_line[f'{i}.txt'] = result
Files_count_line = dict(sorted(Files_count_line.items(), key=lambda item: len(item[1])))
#pprint(Files_count_line, sort_dicts=False)
with open('Total_sorted.txt', 'w', encoding='utf-8') as file:
    for key, value in Files_count_line.items():
            file.write(f'{key}\n')
            file.write(f'{len(value)}\n')
            file.writelines(value)
            file.write('\n')
    print(file)