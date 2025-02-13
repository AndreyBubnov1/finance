class CallbackLexicon():
    def __init__(self, text, data):
        self.tex = text
        self.data = data
                
class Lexicon:
    def __init__(self):
        self.start = "Привет. Это бот для учетa финансов." \
                         " Здесь ты можешь вести журнал " \
                         "своих доходов и расходов," \
                         " а также контролировать свой бюджет"
            
        self.to_fix_transaction = CallbackLexicon(
            text="Зафиксировать транзакцию",
            data="to_fix_transaction"
        )
        self.to_budget_settings = CallbackLexicon(
            text="Настройка бюджета",
            data="to_budget_settings"
        )
        self.to_get_reports= CallbackLexicon(
            text="Отчеты",
            data="to_fix_reports"
        )
        self.select_income = CallbackLexicon(
            text="Доходы",
            data="income_transaction"
        )
        self.select_expence = CallbackLexicon(
            text="Расходы",
            data="expence_transaction"
        )                   
            
lexicon = Lexicon()