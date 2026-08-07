from conf.jsonconf import JsonConf
from conf.promptconf import PromptConf

class Conf:
    def __init__(self, json_path, prompt_path):
        self.json_path = json_path
        self.prompt_path = prompt_path

        self.json_conf = JsonConf(json_path)
        self.prompt_conf = PromptConf(prompt_path)

    def save(self):
        self.json_conf.save()
        self.prompt_conf.save()

        

        