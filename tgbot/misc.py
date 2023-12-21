import asyncio

from aiogram.types import Message

from .keyboards import operationIkb

async def start(message: Message):
    await message.answer(
        text='<b>Выберите действие:</b>',
        reply_markup=operationIkb
    )

async def calculateMessage(message: Message):
    loadChar = '🟩'
    text = '<b>Вычисляю:</b> '
    msg = await message.answer(text)

    for i in range(5):
        text += loadChar

        await msg.edit_text(text)
        await asyncio.sleep(0.2)