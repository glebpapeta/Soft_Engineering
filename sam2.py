import json
import os
from datetime import datetime


class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        """Загрузка расходов из файла"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as file:
                    self.expenses = json.load(file)
                print(f"Загружено {len(self.expenses)} записей о расходах")
            except Exception as e:
                print(f"Ошибка при загрузке файла: {e}")
                self.expenses = []
        else:
            print("Файл с расходами не найден. Будет создан новый.")

    def save_expenses(self):
        """Сохранение расходов в файл"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(self.expenses, file, ensure_ascii=False, indent=2)
            print(f"Данные сохранены в файл: {self.filename}")
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")

    def add_expense(self):
        """Добавление нового расхода"""
        print("\n--- ДОБАВЛЕНИЕ НОВОГО РАСХОДА ---")

        try:
            amount = float(input("Введите сумму расхода: "))
            category = input("Введите категорию расхода: ").strip()
            description = input("Введите описание расхода: ").strip()

            expense = {
                'id': len(self.expenses) + 1,
                'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'amount': amount,
                'category': category,
                'description': description
            }

            self.expenses.append(expense)
            self.save_expenses()
            print("✅ Расход успешно добавлен!")

        except ValueError:
            print("❌ Ошибка: Сумма должна быть числом!")
        except Exception as e:
            print(f"❌ Ошибка при добавлении расхода: {e}")

    def show_expenses(self):
        """Показать все расходы"""
        if not self.expenses:
            print("\n📭 Нет записей о расходах")
            return

        print(f"\n--- ВСЕ РАСХОДЫ (всего: {len(self.expenses)}) ---")
        total = 0

        for expense in self.expenses:
            print(f"ID: {expense['id']}")
            print(f"  Дата: {expense['date']}")
            print(f"  Сумма: {expense['amount']} руб.")
            print(f"  Категория: {expense['category']}")
            print(f"  Описание: {expense['description']}")
            print("-" * 40)
            total += expense['amount']

        print(f"💵 ОБЩАЯ СУММА РАСХОДОВ: {total} руб.")

    def show_statistics(self):
        """Показать статистику по категориям"""
        if not self.expenses:
            print("\n📭 Нет данных для статистики")
            return

        categories = {}
        total = 0

        for expense in self.expenses:
            category = expense['category']
            amount = expense['amount']

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

            total += amount

        print("\n--- СТАТИСТИКА ПО КАТЕГОРИЯМ ---")
        for category, amount in categories.items():
            percentage = (amount / total) * 100
            print(f"  {category}: {amount} руб. ({percentage:.1f}%)")

        print(f"💵 Общая сумма: {total} руб.")

    def show_menu(self):
        """Показать главное меню"""
        print("\n" + "=" * 50)
        print("💰 КНИГА УЧЕТА РАСХОДОВ")
        print("=" * 50)
        print("1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Показать статистику по категориям")
        print("4. Выход")
        print("=" * 50)

    def run(self):
        """Запуск программы"""
        print("Добро пожаловать в программу учета расходов!")

        while True:
            self.show_menu()

            choice = input("Выберите действие (1-4): ").strip()

            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.show_expenses()
            elif choice == '3':
                self.show_statistics()
            elif choice == '4':
                print("До свидания! Данные сохранены.")
                break
            else:
                print("❌ Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
