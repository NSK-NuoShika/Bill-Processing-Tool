from ast import literal_eval
from openai import OpenAI
from src.classifier.classifier import Classifier

class LLMClassifier(Classifier):
    def __init__(self,
                 url: str,
                 key: str,
                 model: str,
                 sys_prompt: str,
                 user_prompt: str) -> None:

        self.model = model
        self.sys_prompt = sys_prompt
        self.user_prompt = user_prompt
        self.client = OpenAI(base_url = url,
                             api_key = key,
                             max_retries = 3)


    def classify(self, data: list[str], category: list[str]) -> tuple[str, ...]:
        response = self.client.chat.completions.create(
            model = self.model,
            messages = [    #  type: ignore
                {
                    'role': 'system',
                    'content': self.sys_prompt
                },
                {
                    'role': 'user',
                    'content': self.user_prompt + '\n' + str(category)
                },
                {
                    'role': 'user',
                    'content': str(data)
                }
            ],

            temperature = 0
        )

        res = literal_eval(response.choices[0].message.content)    # type: ignore

        if not isinstance(res, tuple) or len(res) != len(data):
            raise Exception

        return res
