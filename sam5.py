import datetime


class AttendanceTracker:
    def __init__(self, filename="attendance.txt"):
        self.filename = filename

    def add_student(self, name, student_id):
        """Добавление нового студента"""
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f"СТУДЕНТ|{student_id}|{name}|0|0\n")
        print(f"Студент {name} добавлен")

    def mark_attendance(self, student_id, attended=True):
        """Отметка посещения"""
        lines = []
        found = False

        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith("СТУДЕНТ"):
                    parts = line.strip().split('|')
                    if parts[1] == student_id:
                        total_classes = int(parts[3]) + 1
                        attended_classes = int(parts[4]) + (1 if attended else 0)
                        line = f"СТУДЕНТ|{parts[1]}|{parts[2]}|{total_classes}|{attended_classes}\n"
                        found = True
                lines.append(line)

        if found:
            with open(self.filename, 'w', encoding='utf-8') as file:
                file.writelines(lines)
            status = "присутствовал" if attended else "отсутствовал"
            print(f"Студент {student_id} {status} на занятии {datetime.date.today()}")
        else:
            print("Студент не найден")

    def add_lecture(self):
        """Добавление записи о проведенной лекции"""
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f"ЛЕКЦИЯ|{datetime.datetime.now()}\n")
        print("Запись о лекции добавлена")

    def show_statistics(self):
        """Показать статистику посещаемости"""
        print("\n" + "=" * 50)
        print("СТАТИСТИКА ПОСЕЩАЕМОСТИ")
        print("=" * 50)

        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith("СТУДЕНТ"):
                    parts = line.strip().split('|')
                    student_id, name, total, attended = parts[1], parts[2], parts[3], parts[4]
                    if int(total) > 0:
                        percentage = (int(attended) / int(total)) * 100
                        print(f"{name} ({student_id}): {attended}/{total} ({percentage:.1f}%)")
                    else:
                        print(f"{name} ({student_id}): нет данных о посещениях")

    def find_low_attendance(self, threshold=70):
        """Найти студентов с посещаемостью ниже порога"""
        print(f"\nСтуденты с посещаемостью ниже {threshold}%:")
        print("-" * 40)

        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith("СТУДЕНТ"):
                    parts = line.strip().split('|')
                    student_id, name, total, attended = parts[1], parts[2], parts[3], parts[4]
                    if int(total) > 0:
                        percentage = (int(attended) / int(total)) * 100
                        if percentage < threshold:
                            print(f"{name}: {percentage:.1f}%")

    def show_all_data(self):
        """Показать все данные из файла"""
        print("\nВСЕ ДАННЫЕ ИЗ ФАЙЛА:")
        print("-" * 30)
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                print(file.read())
        except FileNotFoundError:
            print("Файл не найден. Создайте сначала студентов.")


def main():
    tracker = AttendanceTracker()

    print("Создаем базу студентов...")
    students = [
        ("Иванов Алексей", "001"),
        ("Петрова Мария", "002"),
        ("Сидоров Дмитрий", "003"),
        ("Козлова Анна", "004")
    ]

    for name, student_id in students:
        tracker.add_student(name, student_id)

    print("\nОтмечаем посещения...")
    attendance_data = [
        ("001", True), ("002", True), ("003", True), ("004", True),  # Лекция 1
        ("001", True), ("002", False), ("003", True), ("004", True),  # Лекция 2
        ("001", False), ("002", True), ("003", True), ("004", False),  # Лекция 3
        ("001", True), ("002", True), ("003", False), ("004", True),  # Лекция 4
    ]

    for student_id, attended in attendance_data:
        tracker.mark_attendance(student_id, attended)
        tracker.add_lecture()

    tracker.show_statistics()
    tracker.find_low_attendance(75)

    print("\nПример содержимого файла:")
    print("-" * 30)
    tracker.show_all_data()


if __name__ == "__main__":
    main()
