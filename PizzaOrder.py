from Pizza import*
from CustomPizza import*
from SpecialtyPizza import*

class PizzaOrder(CustomPizza, SpecialtyPizza):

    def __init__(self, time):
        '''
        The time format will be stored as an int in a 24-hour time format
        attributes:
        pizzas - a Python List containing all the pizzas that the single order contains. 
        This can be initially set to an empty list
        time - an int representing the expected time the order will be picked up. This field is what will be used in 
        determining the priority of orders. So it is possible for an early order to be deprioritized based on 
        when the pizza is expected to be ready
        '''
        self.time = time
        self.pizzas = []
        
    def getTime(self):
        return self.time
    
    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza=None):
        '''
        will add the Pizza object to the end of the Python List
        '''
        self.pizza = pizza
        self.pizzas.append(pizza)


    def getOrderDescription(self):
        '''
        constructs and returns a string containing the time of the order, all information for each pizza in the order, 
        as well as the total order price. Since we’re storing various Pizza objects in this class, we can utilize 
        polymorphism and simply call the getPizzaDetails() method on the Pizza objects when constructing the string 
        for our entire order, as well as getPrice() to compute the PizzaOrder total price
        '''
        order_description = f'******\nOrder Time: {self.time}\n'
        order_price = 0

        for i in self.pizzas:
            order_description += i.getPizzaDetails()
            #order_description += i.getPizzaDetails()
            order_price += i.getPrice()
            order_description += '\n----\n'

        order_description += f'TOTAL ORDER PRICE: ${order_price:.2f}\n******\n'
        return order_description
