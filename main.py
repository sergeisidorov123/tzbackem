import os


class FinanceRecord:  # Класс для представления одной записи о доходе или расходе

    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"{self.date} | {self.category} | {self.amount} | {self.description}"


class FinanceManager:  # Класс для управления финансами

    def __init__(self, file_path):
        self.file_path = file_path
        self.records = self.load_records()

    def load_records(self):  # Загрузка записей из файла

        records = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                for line in file:
                    date, category, amount, description = line.strip().split('|')
                    records.append(FinanceRecord(date, category, float(amount), description))
        return records

    def save_records(self):  # Сохранение записей в файл

        with open(self.file_path, 'w') as file:
            for record in self.records:
                file.write(f"{record.date}|{record.category}|{record.amount}|{record.description}\n")

    def add_record(self, date, category, amount, description):  # Добавление новой записи

        self.records.append(FinanceRecord(date, category, amount, description))
        self.save_records()

    def edit_record(self, index, date=None, category=None, amount=None, description=None):  # Редактирование существующей записи

        if index < len(self.records):
            if date:
                self.records[index].date = date
            if category:
                self.records[index].category = category
            if amount:
                self.records[index].amount = amount
            if description:
                self.records[index].description = description
            self.save_records()

    def search_records(self, category=None, date=None, amount=None):  # Поиск записей по категории, дате или сумме

        result = []
        for record in self.records:
            if (category and record.category == category) or \
               (date and record.date == date) or \
               (amount and record.amount == amount):
                result.append(record)
        return result

    def get_balance(self):  # Вывод баланса

        income = sum(record.amount for record in self.records if record.category == 'доход')
        expense = sum(record.amount for record in self.records if record.category == 'расход')
        return income - expense

    def get_income(self):  # Вывод доходов

        return sum(record.amount for record in self.records if record.category == 'доход')

    def get_expense(self):  # Вывод расходов

        return sum(record.amount for record in self.records if record.category == 'расход')

    def print_records(self):  # Вывод всех записей

        for i, record in enumerate(self.records, 1):
            print(f"{i}. {record}")


def main():  # Главная функция
    file_path = 'finance_data.txt'
    finance_manager = FinanceManager(file_path)

    while True:
        print("1. Вывод баланса")
        print("2. Вывод доходов")
        print("3. Вывод расходов")
        print("4. Добавление записи")
        print("5. Редактирование записи")
        print("6. Поиск записей")
        print("7. Вывод всех записей")
        print("8. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            print(f"Баланс: {finance_manager.get_balance()}")

        elif choice == '2':
            print(f"Доходы: {finance_manager.get_income()}")

        elif choice == '3':
            print(f"Расходы: {finance_manager.get_expense()}")

        elif choice == '4':
            date = input("Введите дату (YYYY-MM-DD): ")
            category = input("Введите категорию (Доход/Расход): ").lower()
            amount = float(input("Введите сумму: "))
            description = input("Введите описание: ")
            finance_manager.add_record(date, category, amount, description)

        elif choice == '5':
            finance_manager.print_records()
            index = int(input("Введите индекс записи для редактирования: ")) - 1
            date = input("Введите новую дату (YYYY-MM-DD): ")
            category = input("Введите новую категорию (Доход/Расход): ").lower()
            amount = float(input("Введите новую сумму: "))
            description = input("Введите новое описание: ")
            finance_manager.edit_record(index, date, category, amount, description)

        elif choice == '6':
            print("Выберите критерий поиска:")
            print("1. По дате")
            print("2. По категории")
            print("3. По сумме")
            search_choice = input("Введите номер критерия: ")

            if search_choice == '1':
                date = input("Введите дату для поиска (YYYY-MM-DD): ")
                result = finance_manager.search_records(date=date)
            elif search_choice == '2':
                category = input("Введите категорию для поиска (Доход/Расход): ").lower()
                result = finance_manager.search_records(category=category)
            elif search_choice == '3':
                amount = float(input("Введите сумму для поиска: "))
                result = finance_manager.search_records(amount=amount)

            if result:
                for record in result:
                    print(record)
            else:
                print("Ничего не найдено")

        elif choice == '7':
            finance_manager.print_records()

        elif choice == '8':
            break


if __name__ == '__main__':  # Точка входа
    main()
