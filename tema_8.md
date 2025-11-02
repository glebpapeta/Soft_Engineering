# Тема 8. Основы объектно-ориентированного программирования
Отчет по Теме 8 выполнил:

- Папета Глеб Павлович
- АИС-23-1

| Задание | Лаб_раб | Сам_раб |
|---|---|---|
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |


## Лабораторная работа №1.  
### Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Corolla")
```

### Результат.
![Меню](/pic/l1.jpg)

### ВЫВОД.

освоил базовый синтаксис создания классов и их экземпляров

## Лабораторная работа №2. 
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model) :
        self.make = make
        self.model = model
        
    def drive(self):
        print(f"Driving the {self.make} {self.model}")


my_car = Car ("Toyota", "Corolla")
my_car.drive()
```

### Результат.
![Меню](/pic/l2.jpg)

### ВЫВОД.

научился расширять функциональность классов через методы

## Лабораторная работа №3. 
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Михаил А. Панов Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def drive(self):
        print(f"Driving the {self.make} {self.model}")

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
    
    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")


my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()
```

### Результат.
![Меню](/pic/l3.jpg)

### ВЫВОД.

понял принцип создания дочерних классов и переопределения методов

## Лабораторная работа №4. 
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self._make = make
        self.__model = model

    def drive(self):
        print(f"Driving the {self._make} {self.__model}")


my_car = Car ("Toyota", "Corolla")
print(my_car._make)
my_car.drive()
```

### Результат.
![Меню](/pic/l4.jpg)

### ВЫВОД.

 изучил механизмы защиты данных через приватные и защищенные атрибуты

## Лабораторная работа №5. 
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Robot:
    def __init__(self, name):
        self.name = name
    
    def action(self):
        return f"🤖 {self.name} выполняет базовые действия"

class CleanerRobot(Robot):
    def action(self):
        return f"🧹 {self.name} пылесосит пол"

class GuardRobot(Robot):
    def action(self):
        return f"🚨 {self.name} охраняет объект"


robots = [
    Robot("Базовый"),
    CleanerRobot("Чистильщик"),
    GuardRobot("Охранник")
]

for robot in robots:
    print(robot.action())
```

### Результат.
![Меню](/pic/l5.jpg)

### ВЫВОД.

освоил возможность работы с разными типами объектов через единый интерфейс

## Самостоятельная работа №1. 
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class CoffeeDrink:
    def __init__(self, name, price, size="средний"):
        self.name = name
        self.price = price
        self.size = size
        self.is_available = True

    def display_info(self):
        status = "доступен" if self.is_available else "не доступен"
        print(f"☕ {self.name} - {self.price} руб. ({self.size}) - {status}")

    def apply_discount(self, percent):
        new_price = self.price * (100 - percent) / 100
        print(f"Скидка {percent}%: {self.price} → {new_price:.0f} руб.")
        return new_price


latte = CoffeeDrink("Латте", 250)
espresso = CoffeeDrink("Эспрессо", 150, "маленький")

print("=== КОФЕЙНАЯ КАРТА ===")
latte.display_info()
espresso.display_info()

print("\n=== АКЦИИ ===")
latte.apply_discount(15)
espresso.is_available = False
espresso.display_info()
```

### Результат.
![Меню](/pic/s1.jpg)

### ВЫВОД.

закрепил навык проектирования классов для реальных объекто

## Самостоятельная работа №2. 
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class CoffeeDrink:
    def __init__(self, name, price, size="средний"):
        self.name = name
        self.price = price
        self.size = size
        self.is_available = True
        self.brew_strength = "средняя"
        self.milk_type = None
        self.sweetness_level = 0
        self.customizations = []

    def display_info(self):
        status = "доступен" if self.is_available else "не доступен"
        milk_info = f", молоко: {self.milk_type}" if self.milk_type else ""
        sweetness = "без сахара" if self.sweetness_level == 0 else f"сахар: {self.sweetness_level}/10"
        print(f"☕ {self.name} - {self.price} руб. ({self.size})")
        print(f"   Крепость: {self.brew_strength}, {sweetness}{milk_info}")
        print(f"   Статус: {status}")

    def apply_discount(self, percent):
        new_price = self.price * (100 - percent) / 100
        print(f"Скидка {percent}%: {self.price} → {new_price:.0f} руб.")
        return new_price

    def set_brew_strength(self, strength):
        strengths = ["слабая", "средняя", "крепкая", "очень крепкая"]
        if strength in strengths:
            self.brew_strength = strength
            print(f"Крепость {self.name} установлена: {strength}")
        else:
            print("Доступные крепости: слабая, средняя, крепкая, очень крепкая")

    def add_milk(self, milk_type):
        self.milk_type = milk_type
        print(f"Добавлено молоко: {milk_type}")

    def set_sweetness(self, level):
        if 0 <= level <= 10:
            self.sweetness_level = level
            print(f"Уровень сладости установлен: {level}/10")
        else:
            print("Уровень сладости должен быть от 0 до 10")

    def add_customization(self, customization):
        self.customizations.append(customization)
        print(f"Добавлена опция: {customization}")

    def show_customizations(self):
        if self.customizations:
            print(f"Дополнения для {self.name}:")
            for item in self.customizations:
                print(f"   - {item}")
        else:
            print(f"У {self.name} нет дополнительных опций")

    def calculate_brew_time(self):
        times = {"слабая": 2, "средняя": 3, "крепкая": 4, "очень крепкая": 5}
        base_time = times.get(self.brew_strength, 3)
        if self.milk_type:
            base_time += 1
        return base_time


latte = CoffeeDrink("Латте", 250)
espresso = CoffeeDrink("Эспрессо", 150, "маленький")
cappuccino = CoffeeDrink("Капучино", 280, "большой")

print("=== БАЗОВАЯ ИНФОРМАЦИЯ ===")
latte.display_info()
print()
espresso.display_info()

print("\n=== НАСТРОЙКА НАПИТКОВ ===")
latte.set_brew_strength("крепкая")
latte.add_milk("овсяное")
latte.set_sweetness(3)
latte.add_customization("корица")
latte.add_customization("тертый шоколад")

print()
espresso.set_brew_strength("очень крепкая")
espresso.set_sweetness(0)

print()
cappuccino.add_milk("кокосовое")
cappuccino.set_sweetness(7)
cappuccino.add_customization("ванильный сироп")

print("\n=== ИТОГОВАЯ ИНФОРМАЦИЯ ===")
latte.display_info()
print()
espresso.display_info()
print()
cappuccino.display_info()

print("\n=== ДОПОЛНИТЕЛЬНЫЕ ОПЦИИ ===")
latte.show_customizations()
cappuccino.show_customizations()

print("\n=== ВРЕМЯ ПРИГОТОВЛЕНИЯ ===")
print(f"Время приготовления латте: {latte.calculate_brew_time()} мин")
print(f"Время приготовления эспрессо: {espresso.calculate_brew_time()} мин")
print(f"Время приготовления капучино: {cappuccino.calculate_brew_time()} мин")

print("\n=== АКЦИИ ===")
latte.apply_discount(20)
```

### Результат.
![Меню](/pic/s2.jpg)

### ВЫВОД.

научился добавлять специализированные атрибуты и методы

## Самостоятельная работа №3. 
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class CoffeeDrink:
    def __init__(self, name, price, size="средний"):
        self.name = name
        self.price = price
        self.size = size
        self.is_available = True
        self.brew_strength = "средняя"
    
    def display_info(self):
        status = "доступен" if self.is_available else "не доступен"
        print(f"☕ {self.name} - {self.price} руб. ({self.size})")
        print(f"   Крепость: {self.brew_strength}")
        print(f"   Статус: {status}")
    
    def set_brew_strength(self, strength):
        self.brew_strength = strength
        print(f"Крепость {self.name} установлена: {strength}")

class HotCoffee(CoffeeDrink):
    def __init__(self, name, price, size="средний", temperature=85):
        super().__init__(name, price, size)
        self.temperature = temperature
        self.has_foam = False
    
    def add_foam(self):
        self.has_foam = True
        print(f"Добавлена молочная пенка в {self.name}")
    
    def display_info(self):
        super().display_info()
        foam_status = "с пенкой" if self.has_foam else "без пенки"
        print(f"   Температура: {self.temperature}°C, {foam_status}")

class IcedCoffee(CoffeeDrink):
    def __init__(self, name, price, size="большой", ice_amount="среднее"):
        super().__init__(name, price, size)
        self.ice_amount = ice_amount
        self.has_straw = True
    
    def add_syrup(self, syrup_type):
        print(f"Добавлен сироп '{syrup_type}' в {self.name}")
    
    def display_info(self):
        super().display_info()
        straw_status = "с трубочкой" if self.has_straw else "без трубочки"
        print(f"   Лед: {self.ice_amount}, {straw_status}")

print("=== ГОРЯЧИЕ НАПИТКИ ===")
latte = HotCoffee("Латте", 250, "большой", 75)
cappuccino = HotCoffee("Капучино", 280, "средний", 80)
latte.add_foam()
latte.display_info()
print()
cappuccino.display_info()

print("\n=== ХОЛОДНЫЕ НАПИТКИ ===")
iced_latte = IcedCoffee("Айс Латте", 300, "большой", "обильное")
cold_brew = IcedCoffee("Колд Брю", 320, "средний", "минимальное")
iced_latte.add_syrup("ванильный")
iced_latte.display_info()
print()
cold_brew.display_info()

print("\n=== ИЗМЕНЕНИЕ СВОЙСТВ ===")
latte.set_brew_strength("крепкая")
cold_brew.set_brew_strength("слабая")

print("\n=== ПРОВЕРКА ТИПОВ ===")
print(f"Латте является HotCoffee: {isinstance(latte, HotCoffee)}")
print(f"Айс Латте является IcedCoffee: {isinstance(iced_latte, IcedCoffee)}")
print(f"Все являются CoffeeDrink: {isinstance(latte, CoffeeDrink)}")
```

### Результат.
![Меню](/pic/s3.jpg)

### ВЫВОД.

понял как строить логические цепочки наследования для связанных объектов

## Самостоятельная работа №4. 
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class CoffeeDrink:
    def __init__(self, name, price, size="средний"):
        self._name = name
        self._price = price
        self._size = size
        self._is_available = True
        self._brew_strength = "средняя"
        self.__secret_recipe = "базовый рецепт"
        self.__sales_count = 0

    def display_info(self):
        status = "доступен" if self._is_available else "не доступен"
        print(f"☕ {self._name} - {self._price} руб. ({self._size})")
        print(f"   Крепость: {self._brew_strength}")
        print(f"   Статус: {status}")

    def get_name(self):
        return self._name

    def set_price(self, new_price):
        if new_price > 0:
            self._price = new_price
            print(f"Цена изменена на {new_price} руб.")
        else:
            print("Цена должна быть положительной")

    def get_price(self):
        return self._price

    def _change_availability(self, available):
        self._is_available = available
        status = "доступен" if available else "не доступен"
        print(f"Статус изменен: {status}")

    def make_available(self):
        self._change_availability(True)

    def make_unavailable(self):
        self._change_availability(False)

    def __prepare_ingredients(self):
        print(f"Подготавливаются ингредиенты для {self._name}...")

    def __calculate_brew_time(self):
        times = {"слабая": 2, "средняя": 3, "крепкая": 4}
        return times.get(self._brew_strength, 3)

    def prepare_drink(self):
        self.__prepare_ingredients()
        brew_time = self.__calculate_brew_time()
        print(f"Напиток готовится {brew_time} минуты...")
        self.__increment_sales()
        print(f"✅ {self._name} готов!")

    def __increment_sales(self):
        self.__sales_count += 1

    def get_sales_count(self):
        return self.__sales_count

    def _get_secret_recipe(self):
        return f"Секретный рецепт {self._name}: {self.__secret_recipe}"

    def set_brew_strength(self, strength):
        if strength in ["слабая", "средняя", "крепкая"]:
            self._brew_strength = strength
            print(f"Крепость установлена: {strength}")
        else:
            print("Недопустимая крепость")


class PremiumCoffee(CoffeeDrink):
    def __init__(self, name, price, size="средний", origin="Эфиопия"):
        super().__init__(name, price, size)
        self._origin = origin
        self.__aging_months = 12

    def display_info(self):
        super().display_info()
        print(f"   Происхождение: {self._origin}")

    def get_aging_info(self):
        return f"Выдержка: {self.__aging_months} месяцев"

    def _premium_preparation(self):
        print(f"Особая подготовка премиум кофе из {self._origin}")


print("=== БАЗОВЫЙ КЛАСС ===")
latte = CoffeeDrink("Латте", 250)
latte.display_info()

print("\n=== ИНКАПСУЛЯЦИЯ: ГЕТТЕРЫ И СЕТТЕРЫ ===")
print(f"Название напитка: {latte.get_name()}")
print(f"Текущая цена: {latte.get_price()} руб.")
latte.set_price(280)
latte.set_price(-100)

print("\n=== ИНКАПСУЛЯЦИЯ: ДОСТУП К ПРИВАТНЫМ МЕТОДАМ ===")
latte.prepare_drink()
latte.prepare_drink()
print(f"Количество продаж: {latte.get_sales_count()}")

print("\n=== ИНКАПСУЛЯЦИЯ: ЗАЩИЩЕННЫЕ МЕТОДЫ ===")
latte.make_unavailable()
latte.display_info()
latte.make_available()

print("\n=== НАСЛЕДОВАНИЕ И ИНКАПСУЛЯЦИЯ ===")
premium = PremiumCoffee("Эфиопский Премиум", 500, "маленький", "Эфиопия Йиргачеффе")
premium.display_info()
print(premium.get_aging_info())

print("\n=== ПРОВЕРКА ДОСТУПА ===")
try:
    print(latte.__secret_recipe)
except AttributeError as e:
    print(f"Ошибка доступа к приватному атрибуту: {e}")

try:
    print(premium.__aging_months)
except AttributeError as e:
    print(f"Ошибка доступа к приватному атрибуту: {e}")

print("\n=== ИЗМЕНЕНИЕ СВОЙСТВ ===")
latte.set_brew_strength("крепкая")
latte.set_brew_strength("очень крепкая")
latte.display_info()
```

### Результат.
![Меню](/pic/s4.jpg)

### ВЫВОД.

освоил практическое применение инкапсуляции в сложных классах

## Самостоятельная работа №5. 
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class CoffeeDrink:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def prepare(self):
        return f"Готовим базовый напиток {self.name}"
    
    def calculate_serving_time(self):
        return 3
    
    def get_description(self):
        return f"Напиток {self.name} - {self.price} руб."

class Espresso(CoffeeDrink):
    def prepare(self):
        return f"🍩 Варим эспрессо {self.name} под давлением 9 бар"
    
    def calculate_serving_time(self):
        return 2
    
    def get_description(self):
        return f"Крепкий эспрессо {self.name} - {self.price} руб."

class Latte(CoffeeDrink):
    def prepare(self):
        return f"🥛 Готовим латте {self.name} с молочной пенкой"
    
    def calculate_serving_time(self):
        return 4
    
    def get_description(self):
        return f"Нежный латте {self.name} - {self.price} руб."

class ColdBrew(CoffeeDrink):
    def prepare(self):
        return f"🧊 Подаем колд брю {self.name} со льдом"
    
    def calculate_serving_time(self):
        return 1
    
    def get_description(self):
        return f"Освежающий колд брю {self.name} - {self.price} руб."

class TurkishCoffee(CoffeeDrink):
    def prepare(self):
        return f"🔥 Варим турецкий кофе {self.name} в джезве"
    
    def calculate_serving_time(self):
        return 6
    
    def get_description(self):
        return f"Ароматный турецкий кофе {self.name} - {self.price} руб."

def process_coffee_drink(drink):
    print("=" * 40)
    print(drink.get_description())
    print(drink.prepare())
    print(f"Время приготовления: {drink.calculate_serving_time()} мин")
    print(f"Общее время с учетом подачи: {drink.calculate_serving_time() + 1} мин")

def create_coffee_bar(drinks):
    print("🏪 КОФЕЙНАЯ СТОЙКА - ПРОЦЕСС ПРИГОТОВЛЕНИЯ")
    total_time = 0
    for drink in drinks:
        process_coffee_drink(drink)
        total_time += drink.calculate_serving_time()
    print("=" * 40)
    print(f"Общее время приготовления всех напитков: {total_time} мин")

def demonstrate_polymorphism():
    drinks = [
        Espresso("Ристретто", 200),
        Latte("Ванильный латте", 280),
        ColdBrew("Айс кофе", 320),
        TurkishCoffee("По-восточному", 180),
        Espresso("Доппио", 220),
        Latte("Карамельный латте", 300)
    ]
    
    create_coffee_bar(drinks)
    
    print("\n🎯 ДЕМОНСТРАЦИЯ ПОЛИМОРФИЗМА В ДЕЙСТВИИ")
    
    coffee_list = [
        CoffeeDrink("Базовый кофе", 150),
        Espresso("Эспрессо маккиато", 230),
        Latte("Кокосовый латте", 290),
        ColdBrew("Нитро кофе", 350)
    ]
    
    print("\nРазные типы кофе в одном списке:")
    for coffee in coffee_list:
        print(f"- {coffee.prepare()}")
    
    print("\nСравнение времени приготовления:")
    for coffee in coffee_list:
        time = coffee.calculate_serving_time()
        print(f"- {coffee.name}: {time} мин {'⚡' if time < 3 else '⏳'}")

class CoffeeMachine:
    def make_drink(self, coffee_drink):
        print(f"\n☕ КОФЕМАШИНА: {coffee_drink.prepare()}")
        print(f"⏱️  Прогноз: {coffee_drink.calculate_serving_time()} мин")

print("🚀 ЗАПУСК ПРОГРАММЫ С ПОЛИМОРФИЗМОМ")
demonstrate_polymorphism()

print("\n🤖 РАБОТА С КОФЕМАШИНОЙ")
machine = CoffeeMachine()
machine.make_drink(Espresso("Эспрессо", 200))
machine.make_drink(Latte("Латте", 280))
machine.make_drink(ColdBrew("Колд брю", 320))
```

### Результат.
![Меню](/pic/s5.jpg)

### ВЫВОД.

научился создавать системы с взаимозаменяемыми компонентами

### ОБЩИЙ ВЫВОД.

Освоил все основные принципы ООП: инкапсуляцию, наследование и полиморфизм. Научился проектировать классы, создавать иерархии, защищать данные и обеспечивать гибкость кода. Полученные навыки позволяют создавать сложные программные системы с четкой структурой и хорошей поддерживаемостью.
