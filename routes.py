import asyncio

from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from gpt_handler import gpt_response

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет, от команды RealGPT! Напиши мне любое сообщение и я как ГПТ отвечу тебе.")


@router.message()
async def message_handler(msg: Message):
    answer = await gpt_response(prompt=msg.text)
    await msg.answer(answer)


###################################################################
# async def test():
#     answer = await gpt_response(prompt="test value")
#     print(answer)
#
#
# if __name__ == '__main__':
#     asyncio.run(test())
