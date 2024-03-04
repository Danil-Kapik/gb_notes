import json
from datetime import datetime


class Note:
    def __init__(self, id, title, content, create_date, update_date):
        self.id = id
        self.title = title
        self.content = content
        self.create_date = create_date
        self.update_date = update_date

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "create_date": self.create_date.isoformat(),
            "update_date": self.update_date.isoformat(),
        }

    @staticmethod
    def from_dict(note_dict):
        return Note(
            id=note_dict["id"],
            title=note_dict["title"],
            content=note_dict["content"],
            create_date=datetime.fromisoformat(note_dict["create_date"]),
            update_date=datetime.fromisoformat(note_dict["update_date"]),
        )


class Model:
    def __init__(self, file_name="notes.json"):
        self.file_name = file_name
        self.notes = self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.file_name, "r") as file:
                return [Note.from_dict(note_data) for note_data in json.load(file)]
        except FileNotFoundError:
            return []

    def save_to_file(self):
        with open(self.file_name, "w") as file:
            json.dump([note.to_dict() for note in self.notes], file, indent=4)

    def add_note(self, title, content):
        note = Note(len(self.notes) + 1, title, content, datetime.now(), datetime.now())
        self.notes.append(note)
        self.save_to_file()

    def get_all_notes(self):
        return self.notes

    def get_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                return note

    def update_note(self, id, title, content):
        for note in self.notes:
            if note.id == id:
                note.title = title
                note.content = content
                note.update_date = datetime.now()
                self.save_to_file()
                return

    def delete_note(self, id):
        self.notes = [note for note in self.notes if note.id != id]
        self.save_to_file()

    def filter_by_date(self, date):
        return [note for note in self.notes if note.create_date.date() == date.date()]
