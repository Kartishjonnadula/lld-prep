'''
Classes

PizzaBase


Margarita
ChickenPizza

ToppingsDecorater
CheeseTopping
OliveTopping
MushroomTopping
'''
from abc import ABC,abstractmethod
class Pizza(ABC):
    @abstractmethod
    def get_cost(self):
        pass
class MargaritaPizza(Pizza):
    def get_cost(self):
        return 100
class ToppingDecarator(Pizza):
    def __init__(self,pizza):
        self.pizza=pizza

class CheeseTopping(ToppingDecarator):
    topping_price=10
    def get_cost(self):
        return self.pizza.get_cost()+self.topping_price
    
class PizzaSystem:
    def __init__(self):
        self.pizza=None
        self.Toppings=None

    def order_pizza(self,pizza):
        return pizza.get_cost()
    
ps=PizzaSystem()
pizza=MargaritaPizza()
toppingPizza=CheeseTopping(MargaritaPizza())
print(ps.order_pizza(toppingPizza))



