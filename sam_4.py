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
