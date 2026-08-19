class LLMConfig:
    def __init__(self,
                 url: str | None = None,
                 key: str | None = None,
                 model: str | None = None) -> None:

        self.url = url
        self.key = key
        self.model = model



class PromptConfig:
    def __init__(self, sys_prompt: str | None = None, user_prompt: str | None = None) -> None:
        self.user_prompt = user_prompt
        self.sys_prompt = sys_prompt



class BillConfig:
    def __init__(self, category: list[str] | None = None) -> None:
        self.category = category



class Config:
    def __init__(self) -> None:
        self.llmconfig: LLMConfig = LLMConfig()
        self.promptconfig: PromptConfig = PromptConfig()
        self.billconfig: BillConfig = BillConfig()
