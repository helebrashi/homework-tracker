from datetime import date

class Homework:
    def __init__(self, subject: str, due: date):
        self.subject = subject
        self.due = date