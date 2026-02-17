# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime

class Note:
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def __init__(self, code: int, title: str, text: str, importance: str):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_date: datetime = datetime.now()
        self.tags: list[str] = []

    def add_tag(self, tag:str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"-- {self.code} -- {self.title} -- {self.text} -- {self.importance}"

class Notebook:
    def __init__(self):
        self.notes: list[Note] = []

    def add_note(self, title: str, text: str, importance: str) -> int:
        code = len(self.notes) + 1
        while any(note.code == code for note in self.notes): #uso any para el asegurarme de no haber un codigo repetido con false y true
            code += 1
        note = Note(code, title, text, importance)
        self.notes.append(note)
        return code

    def delete_note(self, code: int):
        self.notes.pop(code)

    def important_notes(self) -> list[Note]:
        return [note for note in self.notes if note.importance in (note.HIGH, note.LOW)]

    def notes_by_tags(self, tag: str) -> list[Note]:
        return [note for note in self.notes if tag in note.tags]

    def tag_with_most_notes(self) -> str:
        for note in self.notes:

