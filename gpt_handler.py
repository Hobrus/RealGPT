import openai
from openai import AsyncOpenAI

from config import OPENAI_API_KEY


async def gpt_response(prompt, *kwargs):
    client = AsyncOpenAI(api_key=OPENAI_API_KEY)
    response = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content
