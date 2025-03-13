from datetime import datetime

transactions = {}

def create_transactions(chat_id):
    transactions[chat_id] = get_template_transaction()

def set_type_transaction(chat_id, type_):
    transactions[chat_id]["type"] = type_
    print(transactions)

def get_template_transaction(type_ = None, category = None, amount = None):
    """

    type - тип транзакции
    strftime("%d.%m.%Y") -> дата в формате день месяц год
    """

    return {
        "date": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "type": type_,
        "category": category,
        "amount": amount
    }
res = datetime.now().strftime("%d.%m.%Y %H,%M")
