from bot import bot
from lexicon import lexicon
from keyboards import get_transaction_type_kb, get_expence_categoriers_kb, get_income_categoriers_kb, get_main_menu_kb
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
            message_id=callback.message.message_id,
            reply_markup=get_transaction_type_kb()
        )   
    

    @bot.callback_query_handler(
        func=lambda call: call.data == lexicon.select_income.data
    )
    def to_select_income_categorie(callback):
        chat_id = callback.message.chat.id
        bot.edit_message_text(
            chat_id=chat_id,
            text="123",
            message_id=callback.message.message_id,
            reply_markup=get_income_categoriers_kb()
        )

    @bot.callback_query_handler(
        func=lambda call: call.data == lexicon.select_expence.data
    )
    def to_select_expence_categorie(callback):
        chat_id = callback.message.chat.id
        bot.edit_message_text(
            chat_id=chat_id,
            text="123",
            message_id=callback.message.message_id,
            reply_markup=get_expence_categoriers_kb()
        )

    @bot.callback_query_handler(
        func=lambda call: call.data == lexicon.from_transaction_categorie.data
    )
    def from_transaction_categorie(callback):
        to_fix_transaction(callback)
    

    @bot.callback_query_handler(
        func=lambda call: call.data == lexicon.from_select_transaction_type.data
    )
    def from_select_transaction_type(callback):
        bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            text=lexicon.start,
            reply_markup=get_main_menu_kb()
        )
    