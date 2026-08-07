from openai import OpenAI
import json
from util.tojson import datetime_to_str
from ast import literal_eval


class LLMClassifier:
    def __init__(self, url, key, model, prompt):
        self.client = OpenAI(base_url = url, api_key = key)
        self.prompt = prompt
        self.modle = model


    def classifier(self, bills):
        user_cont = json.dumps(bills, default = datetime_to_str)

        responses = self.client.chat.completions.create(
            model = self.modle,
            messages=[
                {'role':'system', 'content':self.prompt},
                {'role':'user', 'content':user_cont}
            ]
        )
        
        return literal_eval(responses.choices[0].message.content)