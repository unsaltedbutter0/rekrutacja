import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks):
        # TODO zapisz taski do pliku tutaj
        open('taski.json', 'w').write(json.dumps(tasks, ensure_ascii=False, indent=4))
        pass
