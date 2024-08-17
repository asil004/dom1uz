import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, BotCommand
from dotenv import load_dotenv

from constants import START_TEXT
from keyboards import web_button

load_dotenv('.env')

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text=START_TEXT, reply_markup=web_button)


async def main() -> None:
    bot = Bot(token=os.getenv("BOT_TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    commands = [
        BotCommand(command='start', description='Botni ishga tushurish ♻')
    ]
    await bot.set_my_commands(commands)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
