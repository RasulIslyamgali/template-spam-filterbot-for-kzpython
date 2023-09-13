from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType

from config import settings
from utils import get_spam_filter_classes

bot = Bot(token=settings.TG_BOT_API_TOKEN)
dp = Dispatcher(bot)


spam_filter_classes = get_spam_filter_classes()


@dp.message_handler(content_types=ContentType.TEXT)
async def spam_filter(message: types.Message):
    for cls in spam_filter_classes:
        is_spam = cls(message.text).filter()

        if is_spam:
            await message.reply("Это спам")
            break
