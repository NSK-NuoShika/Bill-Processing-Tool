class PromptConf:
    def __init__(self, path):
        self.path = path

        self.load()

    def load(self):
        try:
            self._read()
        except:
            self.conf = DEFAULT_PROMPT
            self._write()


    def save(self):
        self._write()
        

    def _read(self):
        with open(self.path, mode = 'r', encoding = 'utf-8') as f:
            self.conf = f.read()


    def _write(self):
        with open(self.path, mode = 'w', encoding = 'utf-8') as f:
            f.write(self.conf)




DEFAULT_PROMPT="""你是一个个人账单分类器。

用户会输入一个 JSON，每个元素代表一条账单，包含以下字段：
交易时间, 交易对方, 交易商品, 收支类型, 金额

你的任务是为每条账单分类。

输出要求：
1. 只允许输出python元组。
3. 不允许输出任何解释说明。
4. 不允许输出除python元组以外的任何字符。
5. 输出元组长度必须与输入长度一致。
6. 输出顺序必须与输入顺序一致。
7. 每个元素必须为类别。
8. 只能从可选类别中选择

可选类别：
餐饮,购物,交通,生活缴费,医疗,其他

分类注意：
- 类似于超市零食、电商平台消费等的账单归入购物。
- 类似于一日三餐、下午茶等的账单（包括外卖和线下形式的）归入餐饮。
- 类似于铁路、汽车或电动车的充电归入交通。
- 应结合商家和商品说明部分综合判断。
- 对于退款账单，应按照其所属的类别归类，例如超市退款归入购物。
- 对于分类置信度极低的、中性账单（例如银行卡提现、结息等）、无法确定消费商家的、不得已时归入其他。


正确示例：
['购物', '医疗', '其他']
""".strip()