from src.service.config_service import ConfigService
from src.model.config_model import Config


class ConfigController:

    def __init__(self) -> None:
        self.config_service = ConfigService()


    def load(self) -> Config:
        return self.config_service.load()


    def save(self, config: Config) -> None:
        self.config_service.save(config)
