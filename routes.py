from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from gpt_handler import gpt_response

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Напиши мне любое сообщение и я как ГПТ отвечу тебе.")


@router.message()
async def message_handler(msg: Message):
    answer = gpt_response(msg.text)
    # answer = await async_gpt_response(msg.text)
    await msg.answer(answer)
