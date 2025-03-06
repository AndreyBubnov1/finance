from datetime import datetime

transactions = {}

def get_template_data(chat_id, type_, category, amount):
    """
    type - тип транзакции доход или расход "expence" | "income" 
    """
    return {
        "date": datetime.now().strftime("%d.%m.%Y"),
        "chat_id": chat_id,
        "type": type_,
        "categoty": category,
        "amount": amount
    }