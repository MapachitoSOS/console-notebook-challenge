# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.
from datetime import datetime

class Note:
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def __init__(self, code: str, title: str, text: str, importance: str):
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

