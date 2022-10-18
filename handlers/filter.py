from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from config import dp, bot, list_super_admins
from aiogram.dispatcher.filters import BoundFilter


class SuperAdmin(BoundFilter):
    key = 'is_super_admin'

    async def check(self, message: Message) -> bool:

        return str(message.from_user.id) in list_super_admins