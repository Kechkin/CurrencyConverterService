import SetCurrency


class Converter:
    def __init__(self, currency, data=None):
        self.currency = currency
        self.data = data
        self.cur_val = SetCurrency.SetCurrency(self.currency, self.data)
        self.current_value = self.cur_val.get_course()

    def __str__(self):
        return self.cur_val.showCourse()

    def convert_to(self, money):
        res = "%.2f" % (money / self.current_value)
        return f"Конвертирование: {money} рублей - {res} {self.currency}"

    def convert_from(self, money_currency):
        res = "%.2f" % int((money_currency * self.current_value))
        return f"Конвертирование: {money_currency} {self.currency} - {res} рублей"


if __name__ == '__main__':
    user = Converter("Евро", "13.03.2015")
    print(user)
    print(user.convert_to(345))
    print(user.convert_from(5.34))
    user2 = Converter("Доллар США")
    print(user2)
    print(user2.convert_to(145))
    print(user2.convert_from(1.91))
