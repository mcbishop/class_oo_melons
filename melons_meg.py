"""Contains order classes"""

from random import randint

class AbstractMelonOrder(object):
    """A melon order"""

    def __init__(self,species,qty, order_type, tax):
        """Initialize melon order attributes"""
        
        self.species = species
        self.qty = qty
        self.shipped = False       
        self.order_type = order_type
        self.tax = tax
        self.surge_price = False
        self.surge_cost = randint(6,10)

    def get_base_price(self):
        """Splurge pricing uses a random number between 5 and 9."""
        if self.surge_price == True:
            self.base_price = self.surge_cost
        return self.base_price

    def get_total(self,get_base_price):
        """Calculate price."""

        base_price = self.get_base_price
        intl_fee = 0

        if self.species.lower() == "christmas":
            base_price *= 1.50

        if (self.qty < 10 and self.order_type == "international"):
            intl_fee += 3.00
        
        total = ((1 + self.tax) * self.qty * base_price) + intl_fee

        return total

    def mark_surge_price(self):
        """Set surge price to true."""
        self.surge_price = True


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder,self).__init__(species,qty, order_type="domestic", tax=0.08 )
        # self.order_type = "domestic"
        # self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder,self).__init__(species,qty, order_type="international",tax=0.17)
        self.country_code = country_code
        # self.order_type = "international"
        # self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """An order from US Government requiring proper security inspection."""

    def __init__(self,species,qty):
        """Initialize melon order attributes"""
        super(GovernmentMelonOrder,self).__init__(species,qty, order_type="government",tax=0)

    passed_inspection = False

    def inspect_melons(self, passed):
        if passed == True:
            self.passed_inspection = True
        elif passed == False:
            self.passed_inspection = False




