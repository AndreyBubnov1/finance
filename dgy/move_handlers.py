from bot import bot
from lexicon import lexicon
from keyboards import get_transaction_type_kb
from telebot import TeleBot

def register_move_handlers(bot: TeleBot):

    @bot.callback_query_handler(
        func=lambda call: call.data == lexicon.to_fix_transaction.data
        )
    def to_fix_transaction(callback):
        chat_id = callback.message.chat.id
        bot.edit_message_text(
            chat_id=chat_id,
            text="123",
            messge_id=callback.message.message_id,
            reply_markup=get_transaction_type_kb()
        )