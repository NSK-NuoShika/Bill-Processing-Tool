import json
from util import crypt
from copy import deepcopy

class JsonConf:
    def __init__(self, path):
        self.path = path

        self.load()        

    def load(self):
        try:
            self._read()
        except:
            self.conf = DEFAULT_JSON
            self._write()

    def save(self):
        self._write()


    def _read(self):
        with open(self.path, mode = 'r', encoding = 'utf-8') as f:
            self.conf = json.load(f)

        if self.conf['llm']['key']!=None:
            self.conf['llm']['key'] = self._decrypt_llm(self.conf['llm']['key'])


    def _write(self):
        temp_conf = deepcopy(self.conf)

        if temp_conf['llm']['key']!=None:
            temp_conf['llm']['key'] = self._encrypt_llm(self.conf['llm']['key'])

        with open(self.path, mode = 'w', encoding = 'utf-8') as f:
            json.dump(temp_conf, f, ensure_ascii = False, indent = 4)
        

    def _encrypt_llm(self, api_key):
        machine = crypt.get_machineid()
        key = crypt.get_key(machine)
        return crypt.encrypt(key, api_key)


    def _decrypt_llm(self, api_key):
        machineid = crypt.get_machineid()
        key = crypt.get_key(machineid)
        return crypt.decrypt(key, api_key)
    


DEFAULT_JSON = {
    'llm': {
        'url': None,
        'key': None,
        'model': None,
    },

    'category': [
        '餐饮',
        '购物',
        '交通',
        '生活缴费',
        '医疗',
        '其他'
    ]
}





# DEFAULT_JSON = {
#     'llm': {
#         'url': 'https://api.deepseek.com',
#         'key': 'sk-d513477c8ead4482abadf3e3881bf2b8',
#         'model': 'deepseek-v4-flash',
#     },

#     'category': [
#         '餐饮',
#         '购物',
#         '交通',
#         '生活缴费',
#         '医疗',
#         '其他'
#     ]
# }