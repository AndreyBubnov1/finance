from datetime import datetime
transactions = {}

def create_transactions(chat_id):
    transactions[chat_id] = get_template_transaction()

def set_type_transaction(chat_id, type_):
    transactions[chat_id]["type"] = type_
    print(transactions)

def set_categorie_transactions(chat_id, categorie):
    transactions[chat_id]["category"] = categorie
    print(transactions)

def can_set_transaction_amount(chat_id):
    if chat_id in transactions and \
    transactions[chat_id]["type"] is not None and \
    transactions[chat_id]["category"] is not None :
        return True 
    else:
        return False
def get_category(chat_id):
    return transactions[chat_id]["category"]

def set_transaction_amount(chat_id,amount):
    transactions[chat_id]["amount"] = amount
    print(transactions)

def get_transaction_object(chat_id):
    data = transactions[chat_id]
    data["chat_id"] = chat_id
    return data

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
