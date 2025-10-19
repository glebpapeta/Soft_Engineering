def remove_first_occurrence(tuple_data, element_to_remove):

    temp_list = list(tuple_data)

    if element_to_remove in temp_list:
        temp_list.remove(element_to_remove)

    return tuple(temp_list)

my_tuple = (1, 2, 3, 2, 4, 5)
result = remove_first_occurrence(my_tuple, 2)
print(f"Исходный: {my_tuple}")
print(f"После удаления 2: {result}")

result2 = remove_first_occurrence(my_tuple, 6)
print(f"После попытки удалить 6: {result2}")

text_tuple = ("apple", "banana", "cherry", "banana")
result3 = remove_first_occurrence(text_tuple, "banana")
print(f"Текстовый кортеж: {text_tuple}")
print(f"После удаления 'banana': {result3}")
