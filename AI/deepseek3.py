'''
Author: error: git config user.name & please set dead value or install git
Email: error: git config user.email & please set dead value or install git
Date: 2025-02-25 18:35:09
FilePath: /aiagi/AI/deepseek3.py
'''
from openai import OpenAI
import config

client = OpenAI(
    base_url="https://api.deepseek.com/",
    api_key=config.config_data['api_key']
)

completion = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
                "role": "system",
                "content": "你是AI助手"
        },
        {
                "role": "user",
                "content": "请帮我生成一个“爱心”的图案，要圆一点，用JAVA代码生成吧"
        }
    ]
)

print(completion.choices[0].message.content)