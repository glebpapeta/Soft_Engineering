def superset(set_1, set_2):
    if set_1 > set_2:
        print(f'Объект {set_1} является чистым супермножеством')
    elif set_1 == set_2:
        print(f'Множества равны')
    elif set_1 < set_2:
        print(f'Объект {set_2} является чистым супермножеством')
    else:
        print(f'Супермножество не обнаружено')

if __name__ == '__main__':
    superset({1, 2, 5, 7}, {6, 9})
    superset({1, 2, 5, 7}, {5, 3, 8 ,2})
    superset({3, 5}, {5, 3, 8, 1})
    superset({69, 100}, {1, 2})
