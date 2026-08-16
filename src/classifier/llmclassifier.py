from ast import literal_eval
from openai import OpenAI

class LLMClassifier:
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


    def classify(self, data: list[str]) -> tuple[str]:
        response = self.client.chat.completions.create(
            model = self.model,
            messages = [    #  type: ignore
                {
                    'role': 'system',
                    'content': self.sys_prompt,
                },
                {
                    'role': 'user',
                    'content': self.user_prompt + str(data),
                }
            ],
            temperature = 0

        )

        content = response.choices[0].message.content

        return literal_eval(content)    # type: ignore
