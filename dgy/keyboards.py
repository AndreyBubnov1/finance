from telebot import types
from lexicon import lexicon
def get_main_menu_kb():
    button1 = types.InlineKeyboardButton(
        text=lexicon.to_fix_transaction.text,
        callback_data=lexicon.to_fix_transaction.data
    )

    button2 = types.InlineKeyboardButton(
        text=lexicon.to_budget_settings.text,
        callback_data=lexicon.to_budget_settings.data
    )

    button3 = types.InlineKeyboardButton(
        text=lexicon.to_reports.text,
        callback_data=lexicon.to_reports.data
    )



    main_menu_markup = types.InlineKeyboardMarkup()
    main_menu_markup.add(button1)
    main_menu_markup.add(button2)
    main_menu_markup.add(button3)
    return main_menu_markup

def get_transaction_type_kb():
    income_btn = types.InlineKeyboardButton(
        text=lexicon.select_income.text,
        callback_data = lexicon.select_income.data
    )
    expence_btn = types.InlineKeyboardButton(
        text=lexicon.select_expence.text,
        callback_data = lexicon.select_expence.data
    )
    kb = types.InlineKeyboardMarkup()
    kb.add(income_btn)
    kb.add(expence_btn)

    return kb

def remove_old_kb():
    return types.ReplyKeyboardRemove()

