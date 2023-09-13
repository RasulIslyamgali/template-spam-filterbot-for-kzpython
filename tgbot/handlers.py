import datetime as dt

from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType

from config import settings
from utils import get_spam_filter_classes

bot = Bot(token=settings.TG_BOT_API_TOKEN)
dp = Dispatcher(bot)


spam_filter_classes = get_spam_filter_classes()


@dp.message_handler(content_types=ContentType.TEXT)
async def spam_filter(message: types.Message):
    """if is spam ban user and delete message"""

    for cls in spam_filter_classes:
        is_spam = cls(message.text).filter()

        if is_spam:
            user_id = message.from_user.id
            chat_id = message.chat.id

            await message.bot.ban_chat_member(
                chat_id=chat_id,
                user_id=user_id,
                until_date=dt.datetime.today() + dt.timedelta(settings.DEFAULT_BAN_DAYS)
            )
            await message.delete()

            break
