from bot import bot
from handlers.user_handlers import register_user_handlers

register_user_handlers(bot)


bot.polling()