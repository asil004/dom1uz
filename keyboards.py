import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from dotenv import load_dotenv

from constants import BUTTON_TEXT

load_dotenv('.env')

web_button = InlineKeyboardMarkup(
    row_width=True,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=BUTTON_TEXT,
                web_app=WebAppInfo(url=os.getenv('WEB_URL'))
            ),
        ]
    ],
)
