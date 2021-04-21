import urllib.request
import datetime
from xml.dom import minidom


class SetCurrency:
    def __init__(self, currency , data=None):
        self.currency = currency
        self.data = data
        if self.data:
            d, m, y = self.data.split(".")
        else:
            y, m, d = str(datetime.date.today()).split("-")
        self.url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={d}/{m}/{y}'
        self.cur_dict = {}

    def parseCourse(self):
        web_file = urllib.request.urlopen(self.url)
        dom = minidom.parseString(web_file.read())
        dom.normalize()

        elements = dom.getElementsByTagName('Valute')
        for node in elements:
            for child in node.childNodes:
                if child.nodeType == 1:
                    if child.tagName == 'Value':
                        if child.firstChild.nodeType == 3:
                            value = float(child.firstChild.data.replace(',', '.'))
                    if child.tagName == 'Name':
                        if child.firstChild.nodeType == 3:
                            name = child.firstChild.data
            self.cur_dict[name] = value
        return self.cur_dict

    def showCourse(self):
        res = self.parseCourse()
        for key in res.keys():
            if self.currency == key:
                if self.data:
                    return f"Курс {key} на {self.data} - {self.cur_dict[key]} рублей"
                else:
                    return f"Курс {key} на сегодня - {self.cur_dict[key]} рублей"

    def get_course(self):
        res = self.parseCourse()
        for key in res.keys():
            if self.currency == key:
                return self.cur_dict[key]


if __name__ == '__main__':
    user = SetCurrency("Доллар США", "15.04.2021")
    print(user.showCourse())
    print(user.get_course())
