from bot import bot
from lexicon import lexicon
from keyboards import get_transaction_type_kb, get_expence_categoriers_kb, get_income_categoriers_kb, get_main_menu_kb, get_back_to_category_kb
from telebot import TeleBot
from service.tranzaction import create_transactions, set_type_transaction

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
        create_transactions(chat_id)

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
        set_type_transaction(chat_id, lexicon.select_income.text)

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
        set_type_transaction(chat_id, lexicon.select_expence.text)

    @bot.callback_query_handler(
        func=lambda call: call.data == lexicon.from_transaction_categorie.data
    )
    def from_transaction_categorie(callback):
        to_fix_transaction(callback)
    

    @bot.callback_query_handler(
        func=lambda call: call.data in (lexicon.gift_income.data,
                                        lexicon.pocket_income.data,
                                        lexicon.salary_income.data,
                                        lexicon.another_income.data,
                                        lexicon.gift_expence.data,
                                        lexicon.another_expence.data,
                                        lexicon.сlothes_expence.data,
                                        lexicon.transport_expence.data,
                                        lexicon.attractions_expence.data,
                                        lexicon.philanthropy_expence.data,
                                        lexicon.food_expence.data)
    )

    def from_select_transaction_type(callback):
        bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            text="Напишите сумму",
            reply_markup=get_back_to_category_kb()
        )
    