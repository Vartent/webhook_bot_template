# import bot_handlers even if it is unnecessary
from fastapi import FastAPI
from bot import bot, dp
from config import WEBHOOK_URL, WEBHOOK_PATH
from aiogram import Dispatcher, Bot, types
import api.bot_handlers

app = FastAPI()


# creating webhook on app launch
@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)


# webhook to handle updates from telegram api
@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


# do some logic on add shutdown
@app.on_event("shutdown")
async def on_shutdown():
    # Clean up resources here, if necessary
    pass

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
