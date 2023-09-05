import json

from funcs import transformed_date, transformed_from, transformed_to

# открываем json и сортируем его по дате
file = open('operations.json', encoding="utf8")
operations_list = json.load(file)

operations_list_without_empty = [x for x in operations_list if x] # удаляем пустой словарь

operations_sorted = sorted(operations_list_without_empty, key=lambda x: x['date'], reverse=True)
# print(operations_sorted) # for control


# создаем цикл для выведения результатов
counter = 0

for n in operations_sorted:

    if n['state'] == 'EXECUTED':
        counter += 1
        try:
            print(transformed_date(n['date']), n['description'])
            print(f"{transformed_from(n['from'])} ---> {transformed_to(n['to'])}")
            print(n['operationAmount']['amount'], n['operationAmount']['currency']['name'])
            print('\n')

        except KeyError: # если у нас нет даты перевода
            print(f" ---> {transformed_to(n['to'])}")
            print(n['operationAmount']['amount'], n['operationAmount']['currency']['name'])
            print('\n')

        if counter == 5:
            break