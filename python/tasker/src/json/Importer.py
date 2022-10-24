import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        with open('taski.json', 'r') as f:
            self.tasks = json.load(f)
            json.dumps(self.tasks, indent=4, ensure_ascii=False)
        pass

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        return self.tasks
        pass

Importer()