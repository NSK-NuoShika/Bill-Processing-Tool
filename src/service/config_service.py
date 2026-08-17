from src.dao.config_dao import ConfigDao
from src.model.config_model import Config
from src.util.crypt import encrypt, decrypt


class ConfigService:

    def __init__(self, config_file: str) -> None:
        self.json_dao = ConfigDao(config_file)


    def load(self) -> Config:
        conf = Config()

        try:
            data = self.json_dao.read()

            conf.llmconfig.url = data['llm']['url']
            conf.llmconfig.key = None if data['llm']['key'] is None else decrypt(data['llm']['key'])
            conf.llmconfig.model = data['llm']['model']

            conf.promptconfig = data['prompt']
        except:
            self.save(conf)

        return conf


    def save(self, config: Config) -> None:
        data = {
            'llm': {
                'url': config.llmconfig.url,
                'key': None if config.llmconfig.key is None else encrypt(config.llmconfig.key),
                'model': config.llmconfig.model
            },

            'user_prompt': config.promptconfig.user_prompt,
            'bill': {
                'category': config.billconfig.category
            }
        }

        self.json_dao.write(data)
