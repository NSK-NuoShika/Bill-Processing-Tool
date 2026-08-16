import json
from typing import Any


class JsonDao:

    def load(self, json_file: str):
        with open(json_file, "r") as f:
            return json.load(f)


    def write(self, json_file: str, data: dict[Any, Any]):
        with open(json_file, "w") as f:
            f.write(json.dumps(data, indent=4, ensure_ascii = True))
