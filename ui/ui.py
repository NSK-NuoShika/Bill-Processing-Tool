import os
import sys
import subprocess

def input_json_conf_llm(conf):
    conf.json_conf.conf['llm']['url'] = input('请输入URL：').strip()
    conf.json_conf.conf['llm']['key'] = input('请输入key：').strip()
    conf.json_conf.conf['llm']['model'] = input('请输入model：').strip()

def print_json_conf_llm(conf):
    print('url:', conf.json_conf.conf['llm']['url'])
    print('key:', conf.json_conf.conf['llm']['key'])
    print('model:', conf.json_conf.conf['llm']['model'])

def input_json_conf_category(conf):
    conf.json_conf.conf['category'] = list(input('请输入category，并以空格间隔：').split())

def print_json_conf_category(conf):
    print('category:',conf.json_conf.conf['category'])

def input_prompt(conf):
    if sys.platform == 'win32':
        os.startfile(conf.prompt_conf.path)
    elif sys.platform == 'darwin':
        subprocess.run(['open', conf.prompt_conf.path])
    elif sys.platform.startswith("linux"):
        subprocess.run(["xdg-open", conf.prompt_conf.path])

    input('请修改prompt文件，保存后，按回车继续···')

    conf.prompt_conf.load()


def print_prompt(conf):
    print('prompt：\n', conf.prompt_conf.conf)

def input_alipay_path():
    return input('请输入支付宝账单路径：')

def input_wechat_path():
    return input('请输入微信账单路径：').strip()

def input_tar_path():
    return input('请输入输出路径：').strip()

def print_program_running():
    print('程序运行中...')

def print_program_exit():
    print('程序结束！')

