from datetime import datetime


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            self.view.print_menu()
            option = int(input("Выбери опцию: "))
            if option == 1:
                title = input("Введите title: ")
                content = input("Введите content: ")
                self.model.add_note(title, content)
            elif option == 2:
                self.view.print_notes(self.model.get_all_notes())
            elif option == 3:
                id = int(input("Введите ID: "))
                note = self.model.get_note_by_id(id)
                if note:
                    self.view.print_notes([note])
                else:
                    print("Заметка не найдена")
            elif option == 4:
                id = int(input("Введите ID: "))
                title = input("Введите title: ")
                content = input("Введите content: ")
                self.model.update_note(id, title, content)
            elif option == 5:
                id = int(input("Введите ID: "))
                self.model.delete_note(id)
            elif option == 6:
                date_input = input("Введите дату (yyyy-mm-dd): ")
                try:
                    date = datetime.strptime(date_input, "%Y-%m-%d")
                    self.view.print_notes(self.model.filter_by_date(date))
                except ValueError:
                    print("Не верный формат даты! \n")

            elif option == 0:
                break
            else:
                print("Не верная опция")