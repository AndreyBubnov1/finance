from bot import bot
from lexicon import lexicon
from keyboards import get_transaction_type_kb, get_expence_categoriers_kb, get_income_categoriers_kb, get_main_menu_kb, get_back_to_category_kb
from telebot import TeleBot
from service.tranzaction import (create_transactions, set_type_transaction,set_categorie_transactions,
                                 can_set_transaction_amount,set_transaction_amount, get_category,
                                 get_transaction_object)
from service.database import write_database
from service.message import msgs_to_delete
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
        func=lambda call: call.data == lexicon.from_select_transaction_type.data
    )
        def from_select_transactio_type(callback):
            bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            text=lexicon.start,
            reply_markup=get_main_menu_kb()
            )

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

    def from_categorie_to_amount(callback):
        set_categorie_transactions(callback.message.chat.id, callback.data)
        bot.edit_message_text(
            chat_id=callback.message.chat.id,
            text="Напишите сумму",
            message_id=callback.message.message_id,
            reply_markup=get_back_to_category_kb()
        )
        msgs_to_delete[callback.message.chat.id] = callback.message.message_id

    @bot.message_handler(
        func=lambda msg: can_set_transaction_amount(msg.chat.id) and msg.text.isdigit()
    )
    def from_amount_to_main_menu(message):
        amount = int(message.text)
        chat_id=message.chat.id
        set_transaction_amount(chat_id, amount)

        data = get_transaction_object(chat_id)
        write_database(data)
        
        bot.delete_message(
            chat_id=chat_id,
            message_id=message.message_id
        )

        bot.delete_message(
            chat_id=chat_id,
            message_id=message.message_id
        )

        bot.send_message(
            chat_id=chat_id,
            text=lexicon.fixed_transaction.format_map(data)
        )
        bot.send_message(
            chat_id=chat_id,
            text=lexicon.start,
            reply_markup=get_main_menu_kb()
        )


    def error_input_amount(message):
        bot.delete_message(
            chat_id=message.chat.id,
            message_id=message.message_id
        )
    @bot.callback_query_handler(
        func=lambda call: call.data == lexicon.from_amount_to_categorie.data
    )
    @bot.callback_query_handler(
        func= lambda call: call.data == lexicon.from_amount_to_categorie.data
    )
    def from_amount_to_categorie(callback):
        category = get_category(callback.message.chat.id)
        if category.endswith("income"):
            kb =  get_income_categoriers_kb()
        elif category.endswith("expence"):
            kb = get_expence_categoriers_kb()
        bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            text="Напишите сумму",
        )