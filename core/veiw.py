class View:
    @staticmethod
    def print_menu():
        print("1. Создание заметки")
        print("2. Чтение всех заметок")
        print("3. Чтение заметки")
        print("4. Редактирование заметки")
        print("5. Удаление заметки")
        print("6. Фильтрация по дате")
        print("0. Выход")

    @staticmethod
    def print_notes(notes):
        for note in notes:
            print(f"ID: {note.id}, Title: {note.title}, Content: {note.content}, Create Date: {note.create_date}")

