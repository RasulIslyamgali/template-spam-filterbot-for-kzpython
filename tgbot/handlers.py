from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType

from config import settings

bot = Bot(token=settings.TG_BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=ContentType.TEXT)
async def spam_filter(message: types.Message):
    await message.reply("Это спам")
