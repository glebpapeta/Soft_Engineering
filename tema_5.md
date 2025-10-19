# Тема 6. Базовые коллекции: словари, кортежи.
Отчет по Теме 6 выполнил:

* Папета Глеб Павлович
* АИС-23-1

| Задание | Лаб_раб | Сам_раб |
|---|---|---|
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |


# Лабораторная работа №6.  
## 1) В школе, где вы учились, узнали, что вы крутой программист и попросили написать программу для учителей, которая будет при вводе кабинета писать для него ключ доступа и статус, занят кабинет или нет. При написании программы необходимо использовать словарь (dict), который на вход получает номер кабинета, а выводит необходимую информацию. Если кабинета, который вы ввели нет в словаре, то в консоль в виде значения ключа нужно вывести “None” и виде статуса вывести “False”. По большому счету написав данную программу мы с вами научились заменять иногда громоздкую конструкцию if/elif/else. Поскольку здесь функционал словаря полностью повторяет функционал условия, но при этом у использования словарей в более сложных программах есть намного больше возможностей реализации
```python
request = int(input("Введите номер кабинета: "))
dictionary = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1337, 'access': True},
    103: {'key': 8943, 'access': True},
    104: {'key': 5555, 'access': False},
    None: {'key': None, 'access': False},
}
response = dictionary.get(request)
if not response:
    response = dictionary[None]
key = response.get ("key")
access = response.get('access')
print(key, access)
```

![Скриншот выполнения](/pic/l1.png)

## 2) Алексей решил создать самый большой словарь в мире. Для этого он придумал функцию dict_maker (**kwargs), которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict, состоящий всего из одного элемента «first» со значением «so easy». Помогите Алексею создать данную функцию. Ниже на скриншоте мы использовали встроенный модуль pprint, который выводит большие объемы информации более понятно для восприятия человеческим глазом. Иногда очень удобно использовать данную возможность Python. 
```python
from pprint import pprint

my_dict = {'first': 'so easy'}

def dict_maker(**kwargs):
    my_dict.update(**kwargs)

dict_maker(a1=1, a2=20, a3=54, a4=13)
dict_maker(name="Михаил", age=31, weight=70, eyes_color="blue")
pprint (my_dict)
```
![Скриншот выполнения](/pic/l2.png)

## 3) Для решения некоторых задач бывает необходимо разложить строку на отдельные символы. Мы знаем что это можно сделать при помощи split(), у которого более гибкая настройка для разделения для этого, но если нам нужно посимвольно разделить строку без всяких условий, то для этого мы можем использовать кортежи (tuple). Для этого напишем любую строку, которую будем делить и “обвернем” ее в tuple и дальше мы можем как нам угодно с ней работать, например, сделать ее списком (тогда получится полный аналог split()) или же работать с ним дальше, как с кортежем.

```python
input_string = 'HelloWorld'
result = tuple(input_string)
print(result)
print(list(result))
```

![Скриншот выполнения](/pic/l3.png)

## 4) Вовочка решил написать крутую функцию, которая будет писать имя, возраст и место работы, но при этом на вход этой функции будет поступать кортеж. Помогите Вовочке написать эту программу
```python
def personal_info(name, age, company="unnamed"):
    print(f"Иня: {name} Возраст: {age} Компания: {company}")

tom = ("Григорий", 22)
personal_info(*tom)
bob = ("Георгий", 41, "Yandex")
personal_info(*bob)
```
![Скриншот выполнения](/pic/l4.png)

## 5) Для сопровождения первых лиц государства X нужен кортеж, но никто не может определиться с порядком машин, поэтому вам нужно написать функцию, которая будет сортировать кортеж, состоящий из целых чисел по возрастанию, и возвращает его. Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.

```python
def tuple_sort(tpl):
    for elm in tpl:
        if not isinstance(elm, int):
            return tpl
    return tuple(sorted(tpl))

if __name__ == '__main__':    
    print(tuple_sort((5, 5, 3, 1, 9)))
    print(tuple_sort((5, 5, 2.1, '1', 9)))
```
![Скриншот выполнения](/pic/l5.png)


# Самостоятельная работа №6. 

## 1) При создании сайта у вас возникла потребность обрабатывать данные пользователя в странной форме, а потом переводить их в нужные вам форматы. Вы хотите принимать от пользователя последовательность чисел, разделенных пробелом, а после переформатировать эти данные в список и кортеж. Реализуйте вашу задумку. Для получения начальных данных используйте input(). Результатом программы будет выведенный список и кортеж из начальных данных.
```python
user_input = input("Введите числа через пробел: ")
numbers_list = [int(x) for x in user_input.split()]
numbers_tuple = tuple(numbers_list)
print(numbers_list)
print(numbers_tuple)
```
![Скриншот выполнения](/pic/s1.png)

Вывод: узнал как преобразовывать строку в список чисел через split() и создавать кортежи из списков.


## 2) Николай знает, что кортежи являются неизменяемыми, но он очень упрямый и всегда хочет доказать, что он прав. Студент решил создать функцию, которая будет удалять первое появление определенного элемента из кортежа по значению и возвращать кортеж без него. Попробуйте повторить шедевр не признающего авторитеты начинающего программиста. Но учтите, что Николай не всегда уверен в наличии элемента в кортеже (в этом случае кортеж вернется функцией в исходном виде).
```python
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
```
![Скриншот выполнения](/pic/s2.png)

Вывод: научился работать с неизменяемыми кортежами - преобразовывать в список для изменений и обратно в кортеж.

## 3) Ребята поспорили кто из них одним нажатием на numpad наберет больше повторяющихся цифр, но не понимают, как узнать победителя. Вам им нужно в этом помочь. Дана строка в виде случайной последовательности чисел от 0 до 9 (длина строки минимум 15 символов). Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте функцию, принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел, также эти значения нужно вывести в порядке возрастания ключа.
```python
def count_top_three_digits(digit_string):

    digit_count = {}

    for char in digit_string:
        digit = int(char)
        digit_count[digit] = digit_count.get(digit, 0) + 1

    sorted_digits = sorted(digit_count.items(), key=lambda x: (-x[1], x[0]))

    top_three = dict(sorted_digits[:3])

    print("Три самые частые цифры (в порядке возрастания ключа):")
    for digit in sorted(top_three.keys()):
        print(f"Цифра {digit}: встречается {top_three[digit]} раз")

    return top_three

test_string = "123456789012345678901234567890"
print(f"Исходная строка: {test_string}")

result = count_top_three_digits(test_string)
print(f"\nСловарь с результатами: {result}")
```
![Скриншот выполнения](pic/s3.png)

Вывод: понял как считать частоту элементов через словарь и сортировать по нескольким критериям (частота и ключ).

## 4) Ваш хороший друг владеет офисом со входом по электронным картам, ему нужно чтобы вы написали программу, которая показывала в каком порядке сотрудники входили и выходили из офиса. Определение сотрудника происходит по id. Напишите функцию, которая на вход принимает кортеж и случайный элемент (id), его можно придумать самостоятельно. Требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно. Если элемента нет вовсе – вернуть пустой кортеж. Если элемент встречается только один раз, то вернуть кортеж, который начинается с него и идет до конца исходного
```python
def get_employee_interval(access_log, employee_id):

    if employee_id not in access_log:
        return ()

    first_index = access_log.index(employee_id)

    try:
        second_index = access_log.index(employee_id, first_index + 1)

        return access_log[first_index:second_index + 1]
    except ValueError:

        return access_log[first_index:]


def test_system():

    office_access_log = (101, 102, 103, 101, 104, 105, 102, 106, 103, 101, 107)

    print("Полный лог доступа в офис:")
    print(office_access_log)
    print("\n" + "=" * 50 + "\n")

    employee1 = 101
    result1 = get_employee_interval(office_access_log, employee1)
    print(f"Сотрудник {employee1}: {result1}")
    print(f"Первый вход и до второго выхода: {len(result1)} записей\n")

    employee2 = 107
    result2 = get_employee_interval(office_access_log, employee2)
    print(f"Сотрудник {employee2}: {result2}")
    print(f"Только один вход: {len(result2)} записей\n")

    employee3 = 999
    result3 = get_employee_interval(office_access_log, employee3)
    print(f"Сотрудник {employee3}: {result3}")
    print(f"Не было доступа: {len(result3)} записей\n")

    employee4 = 102
    result4 = get_employee_interval(office_access_log, employee4)
    print(f"Сотрудник {employee4}: {result4}")
    print(f"Первый вход и до второго выхода: {len(result4)} записей")


def analyze_all_employees(access_log):
    unique_employees = set(access_log)

    print("\nАнализ всех сотрудников:")
    print("-" * 40)

    for emp_id in sorted(unique_employees):
        interval = get_employee_interval(access_log, emp_id)
        visits = access_log.count(emp_id)

        if visits == 1:
            status = "Был один раз"
        elif len(interval) > 0:
            status = f"Интервал: {len(interval)} записей"
        else:
            status = "Не было доступа"

        print(f"Сотрудник {emp_id}: {visits} посещений, {status}")


if __name__ == "__main__":
    test_system()

    office_log = (101, 102, 103, 101, 104, 105, 102, 106, 103, 101, 107)
    analyze_all_employees(office_log)
```
![Скриншот выполнения](/pic/s4.png)

Вывод: узнал как находить индексы элементов в кортеже и делать срезы между определенными позициями.


## 5) Самостоятельно придумайте и решите задачу, в которой будут обязательно использоваться кортеж или список. Проведите минимум три теста для проверки работоспособности вашей задачи.
```python
def calculate_student_grades(students, subjects, grades):
    subject_averages = {}

    for i, subject in enumerate(subjects):
        subject_grades = []
        for student_grades in grades:
            if i < len(student_grades):
                subject_grades.append(student_grades[i])
        if subject_grades:
            subject_averages[subject] = sum(subject_grades) / len(subject_grades)

    student_totals = []
    for i, student in enumerate(students):
        if i < len(grades):
            student_total = sum(grades[i])
            student_average = student_total / len(grades[i]) if grades[i] else 0
            student_totals.append((student, student_total, round(student_average, 2)))

    top_student = max(student_totals, key=lambda x: x[2]) if student_totals else ("", 0, 0)

    return {
        'subject_averages': subject_averages,
        'student_results': student_totals,
        'top_student': top_student
    }


def print_results(results):
    print("Средние баллы по предметам:")
    for subject, avg in results['subject_averages'].items():
        print(f"{subject}: {avg:.2f}")

    print("\nРезультаты студентов:")
    for student, total, avg in results['student_results']:
        print(f"{student}: сумма = {total}, средний = {avg}")

    print(f"\nЛучший студент: {results['top_student'][0]} со средним баллом {results['top_student'][2]}")


students1 = ["Иван", "Мария", "Петр"]
subjects1 = ["Математика", "Физика", "Химия"]
grades1 = [
    [5, 4, 3],
    [4, 5, 5],
    [3, 4, 4]
]

students2 = ["Анна", "Сергей"]
subjects2 = ["История", "Литература"]
grades2 = [
    [5, 5],
    [4, 3]
]

students3 = ["Ольга"]
subjects3 = ["Биология", "География", "Английский"]
grades3 = [
    [5, 4, 5]
]

print("ТЕСТ 1:")
result1 = calculate_student_grades(students1, subjects1, grades1)
print_results(result1)

print("\n" + "=" * 50)
print("ТЕСТ 2:")
result2 = calculate_student_grades(students2, subjects2, grades2)
print_results(result2)

print("\n" + "=" * 50)
print("ТЕСТ 3:")
result3 = calculate_student_grades(students3, subjects3, grades3)
print_results(result3)
```
![Скриншот выполнения](/pic/s5.png)

Вывод: закрепил базовые операции со списками - добавление, удаление, проверка наличия элементов.


# Вывод 
Освоил основные операции со словарями и кортежами, решил задачи где они используются.
