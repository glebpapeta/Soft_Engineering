import datetime
import time

for i in range(5):
    # Получаем текущее время
    current_time = datetime.datetime.now()

    # Форматируем время в строку (часы:минуты:секунды)
    formatted_time = current_time.strftime("%H:%M:%S")

    # Выводим текущее время
    print(formatted_time)

    # "Усыпляем" программу на 1 секунду
    time.sleep(1)
