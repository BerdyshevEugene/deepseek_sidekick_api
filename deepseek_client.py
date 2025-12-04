import os
from openai import OpenAI

from config import config_obj


def get_answer_from_deepseek(prompt: str):
    client = OpenAI(api_key=config_obj.deepseek_api_key, base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )

    return response.choices[0].message.content
