import asyncio
import logging
import sys
from enum import Enum

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from api import get_recommended

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6556058793:AAHAoK2JrULRAeVw7xyM963ozYrxaaCKqSw"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id

    meme = get_recommended(user_id)

    like_btn = InlineKeyboardButton(text="👍", callback_data=f"like_{meme.hashsum}")
    disl_btn = InlineKeyboardButton(text="👎", callback_data=f"dislike_{meme.hashsum}")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[like_btn, disl_btn]])
    await message.answer_photo(
        str(meme.image_url),
        caption=meme.description,
        reply_markup=keyboard,
    )


@dp.callback_query()
async def reaction_handler(query: CallbackQuery):
    print(query)


@dp.message()
async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
