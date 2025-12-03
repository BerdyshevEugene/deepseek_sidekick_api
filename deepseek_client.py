import os
from openai import OpenAI

from config import config_obj


def main():
    client = OpenAI(api_key=config_obj.deepseek_api_key, base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "привет как дела"},
        ],
        stream=False
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()