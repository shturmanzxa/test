import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

# Берём токен из Render → Environment Variables
TOKEN = os.getenv("TOKEN")
ADMIN_ID = 8219175129  # <- Твой айди

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Бот работает 24/7 и шлёт сообщение админу каждую минуту!")


# Функция, которая шлёт сообщение каждый X секунд
async def periodic_sender():
    await bot.wait_until_ready() if hasattr(bot, "wait_until_ready") else None

    while True:
        try:
            await bot.send_message(ADMIN_ID, "Твой ID: 8219175129")
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")

        await asyncio.sleep(60)  # <-- каждую минуту


async def on_startup(dp):
    asyncio.create_task(periodic_sender())
    print("Бот запущен и автопуш каждые 60 секунд включён!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

