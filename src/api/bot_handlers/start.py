from bot import dp
from aiogram.types import Message


# initial bot command
@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    await message.answer(text='hello there')