from pathlib import Path

PROJECT_ROOT_PATH = Path(__file__).parents[2].resolve()

def load_sys_prompt() -> str:
    with open(PROJECT_ROOT_PATH / 'resources' / 'sys_prompt.txt', mode = 'r', encoding = 'utf-8') as f:
        return f.read().strip()
