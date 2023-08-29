# Auxiliary functions

def transformed_from(number):
    """функция принимает номер карты отправителя и выдает в нужном формате"""
    num_list = list(number)
    new_list1 = []
    new_list2 = []
    for num in num_list:
        str_n = str(num)
        if str_n.isalpha() or str_n.isspace() == True:
            new_list1.append(str_n) # list for words
        elif str_n.isalpha() or str_n.isspace() == False:
            new_list2.append(str_n) # list for numbers
    first_part = "".join(new_list2[:4])
    second_part = "".join(new_list2[5:6])
    last_part = "".join(new_list2[-4:])
    word = "".join(new_list1)

    return f"{word}{first_part} {second_part}** **** {last_part}"

# num = "MasterCard 3152479541115065" # for control
# num = "Счет 27248529432547658655" # for control
# b = transformed_from(num)
# print(b)


def transformed_to(number):
    """функция принимает номер счета и выдает в нужном формате"""
    required_num = "Счет**XXXX"
    num_list = list(number)
    new_list1 = []
    new_list2 = []
    for num in range(-4, 0):
        new_list1.append(num_list[num])

    for num in num_list:
        str_n = str(num)
        if str_n.isalpha() or str_n.isspace() == True:
            new_list2.append(str_n)

    a = required_num.replace("XXXX", "".join(new_list1))
    fin = a.replace("Счет", "".join(new_list2))

    return fin

# num = "Счет 43597928997568165086" # for control
# num2 = "Visa Gold 9447344650495960" # for control
# b = transformed_to(num2) # for control
# print(b)

