import json
from typing import Any


class ConfigDao:

    def __init__(self, json_file: str = "config.json") -> None:
        self.json_file = json_file


    def read(self):
        with open(self.json_file, "r", encoding = 'utf-8') as f:
            return json.load(f)


    def write(self, data: dict[Any, Any]):
        with open(self.json_file, "w", encoding = 'utf-8') as f:
            f.write(json.dumps(data, indent = 4, ensure_ascii = False))
