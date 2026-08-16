from src.dao.json_dao import JsonDao
from src.model.config_model import Config
from src.util.crypt import encrypt, decrypt


class ConfigService:

    def __init__(self, json_dao: JsonDao) -> None:
        self.json_dao = json_dao


    def load(self, config_file: str) -> Config:
        conf = Config()

        try:
            data = self.json_dao.load(config_file)

            conf.llmconfig.url = data['llm']['url']
            conf.llmconfig.key = None if data['llm']['key'] is None else decrypt(data['llm']['key'])
            conf.llmconfig.model = data['llm']['model']

            conf.promptconfig = data['prompt']
        except:
            self.save(conf, config_file)

        return conf


    def save(self, conf: Config, config_file: str) -> None:
        data = {
            'llm': {
                'url': conf.llmconfig.url,
                'key': None if conf.llmconfig.key is None else encrypt(conf.llmconfig.key),
                'model': conf.llmconfig.model
            },

            'user_prompt': conf.promptconfig.user_prompt,
            'bill': {
                'category': conf.billconfig.category
            }
        }

        self.json_dao.write(config_file, data)
