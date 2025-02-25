'''
Author: error: git config user.name & please set dead value or install git
Email: error: git config user.email & please set dead value or install git
Date: 2025-02-25 18:35:09
FilePath: /aiagi/AI/test copy.py
'''
from openai import OpenAI

client = OpenAI(
    base_url="https://api.deepseek.com/",
    api_key="sk-f0de4496937d4a53925e031013e24c16"
)

completion = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
                "role": "system",
                "content": "你是一位大模型提示词生成专家，请根据用户的需求编写一个智能助手的提示词，来指导大模型进行内容生成，要求：\n1. 以 Markdown 格式输出\n2. 贴合用户需求，描述智能助手的定位、能力、知识储备\n3. 提示词应清晰、精确、易于理解，在保持质量的同时，尽可能简洁\n4. 只输出提示词，不要输出多余解释"
        },
        {
                "role": "user",
                "content": "请帮我生成一个“Linux 助手”的提示词"
        }
    ]
)

print(completion.choices[0].message.content)