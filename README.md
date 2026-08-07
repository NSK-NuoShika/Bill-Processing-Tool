**Currently only Simplified Chinese is supported; other languages will be available in future versions.**

# 账单管理系统

## 概述

本项目旨在解决多平台账单格式不一致，原生平台账单分类方案不满足个性化需求等多种问题。

程序读取 Excel 格式的支付宝和微信账单，合并为总账单，并按类别分类。分类功能基于大模型调用，精准识别每条账单类别，模型配置持久化存储于本地配置文件，创造性地通过获取设备 GUID 为模型 API 密钥配置加密，解决密钥泄露等安全性问题

目前仅支持通过 LLM 调用进行分类，仅支持 OpenAi 兼容的接口，其他分类方式、多语言版本、其他平台账单支持、其他模型接口支持将在后续版本推出。



## 构建方法

1. 安装根目录下 `requirements.txt` 中的依赖。先将终端目录 `cd` 到本项目根目录，在终端执行：
   ```bash
   pip install -r requirements.txt
   ```

2. 在项目根目录下运行 `main.py` 文件即可。

## 使用方法

1. 在微信和支付宝导出账单。
2. 手动打开 `csv` 格式的支付宝账单，另存为 `xlsx（Excel）` 格式。
3. 根据程序提示读入模型配置、账单绝对路径。
4. 等待完成即可。

## 许可证

本项目使用 MIT 许可。

   

