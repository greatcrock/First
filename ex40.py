"""
Вы - владелец кафе, в котором работают 3 повара: JapaneseCook, RussianCook и ItalianCook.
Каждый из них умеет готовить блюдо и напиток национальной кухни:
- JapaneseCook: Sushi и Tea
- RussianCook: Dumplings и Compote
- ItalianCook: Pizza и Juice
Ваша задача - реализовать 3 класса (каждый повар - отдельный класс),
которые будут наследниками AbstractCook с соответствующими методами:
- add_food(food_amount, food_price), который добавляет в заказ клиента указанное количество еды по указанной цене
- add_drink(drink_amount, drink_price), который добавляет в заказ клиента указанное количество напитков по указанной цене
- total(), который возвращает строку вида: 'Food: 150, Drinks: 50, Total: 200',
причем для каждого повара на месте Food и Drinks будут указаны именно те блюда и напитки, которые он готовит.
Обратите внимание, что каждый клиент может обращаться только к одному повару. В этой миссии вам может помочь такой
шаблон проектирования, как Abstract Factory .
"""

"""
В этом задании все входные данные коректны, и проверку значений можно не выполнять.

Входные данные: операторы и выражения, использующие классы 3 поваров.
Выходные данные: строка, описывающая заказ и сумма для оплаты.

Как это используется: Работа с классами и объектно-ориентированным программированием - более высокий уровень мастерства, 
которым следует овладеть, чтобы иметь возможность использовать Python в полной мере.

Предусловие: Все данные корректны.
"""


"""
Example :

client_1 = JapaneseCook()
client_1.add_food(2, 20)
client_1.add_drink(5, 4)
client_1.total() == "Sushi: 40, Tea: 20, Total: 60"

client_2 = RussianCook()
client_2.add_food(1, 40)
client_2.add_drink(5, 20)
client_2.total() == "Dumplings: 40, Compote: 100, Total: 140"

client_3 = ItalianCook()
client_3.add_food(2, 20)
client_3.add_drink(2, 10)
client_3.total() == "Pizza: 40, Juice: 20, Total: 60"
"""


class AbstractCook:
    def __init__(self):
        self.drink = 0
        self.food = 0

    def add_food(self, amount, price):
        self.food += int(amount) * int(price)

    def add_drink(self, amount, price):
        self.drink += int(amount) * int(price)


class JapaneseCook(AbstractCook):
    def total(self):
        return f"Sushi: {self.food}, Tea: {self.drink}, Total: {self.drink + self.food}"


class RussianCook(AbstractCook):
    def total(self):
        return f"Dumplings: {self.food}, Compote: {self.drink}, Total: {self.drink + self.food}"


class ItalianCook(AbstractCook):
    def total(self):
        return f"Pizza: {self.food}, Juice: {self.drink}, Total: {self.drink + self.food}"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
    print("Coding complete? Let's try tests!")        

word = "Hello"
print(word.find("a") + 1)