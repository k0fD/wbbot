from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message

import kb
import text

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.keyboard)


@router.message()
async def but1(msg: Message):
    if msg.text == "Кнопка 1":
        await msg.answer('Услышал 1 кнопку')
    elif msg.text == "Кнопка 2":
        await msg.answer('Услышал 2 Кнопку')
    elif msg.text == "Кнопка 3":
        await msg.answer('Услышал 3 кнопку')
