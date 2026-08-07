from conf.conf import Conf
from util.terminal import clean_screen
from ui.ui import *
from opbill.alipay import Alipay
from opbill.wechat import Wechat
from opbill.bill import Bill
from classifier.llm_classifier import LLMClassifier


clean_screen()

input('账单分类器启动，请按回车继续...')

clean_screen()

cf = Conf(json_path = 'conf.json', prompt_path = 'prompt.txt')

if cf.json_conf.conf['llm']['url'] == None or cf.json_conf.conf['llm']['key'] ==  None or cf.json_conf.conf['llm']['model'] == None:
    input_json_conf_llm(cf)
    print()

if cf.json_conf.conf['category'] == None:
    input_json_conf_category()
    input_prompt()
    print()


while True:
    print('以下是配置：')
    print_json_conf_llm(cf)
    print_json_conf_category(cf)
    print_prompt(cf)
    print()

    r1 = input('输入Y/N确认:').strip().upper()

    if r1 == 'Y':
        break
    elif r1 == 'N':
        clean_screen()

        print('1. 修改模型配置')
        print('2. 修改种类配置')
        print('3. 修改提示词配置')
        print()

        while True:
            r2 = input('请输入编号：').strip()
            print()

            if r2 == '1':
                clean_screen()
                input_json_conf_llm(cf)
                clean_screen()
                break
            elif r2 == '2':
                clean_screen()
                input_json_conf_category(cf)
                clean_screen()
                break
            elif r2 == '3':
                clean_screen()
                input_prompt(cf)
                clean_screen()
                break
            else:
                print('输入非法！')
    else:
        clean_screen()
        print('输入非法！')
        print()

cf.save()

cla = LLMClassifier(url=cf.json_conf.conf['llm']['url'], key=cf.json_conf.conf['llm']['key'], model=cf.json_conf.conf['llm']['model'], prompt=cf.prompt_conf.conf)

clean_screen()

ali_path = input_alipay_path()
wec_path = input_wechat_path()
tar_path = input_tar_path()

clean_screen()

print_program_running()

ali = Alipay(ali_path)
wec = Wechat(wec_path)

ali.hand()
wec.hand()

bil = Bill(cf.json_conf.conf['category'], wec, ali)
bil.classify(cla.classifier, 500)
bil.save(tar_path)

clean_screen()

print_program_exit()