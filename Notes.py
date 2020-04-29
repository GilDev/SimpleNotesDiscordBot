import json
import os


class Notes:
    _path = ""
    _notes = {}

    def __init__(self, path):
        self._path = path
        try:
            with open(self._path, "r") as f:
                self._notes = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass

    def getAll(self):
        return self._notes

    def get(self, name):
        return self._notes[name] if name in self._notes else False

    def write(self, name, content):
        self._notes[name] = content
        self._save()

    def delete(self, name):
        if name in self._notes:
            del self._notes[name]
            self._save()
            return True

        return False

    def _save(self):
        os.makedirs(os.path.dirname(self._path), exist_ok=True)
        with open(self._path, "w") as f:
            json.dump(self._notes, f)
