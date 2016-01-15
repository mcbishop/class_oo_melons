"""Contains order classes"""


class AbstractMelonOrder(object):
    """A melon order"""

    def __init__(self,species,qty):
        """Initialize melon order attributes"""
        
        self.species = species
        self.qty = qty
        self.shipped = False       

    def get_total(self):
        """Calculate price."""

        base_price = 5
        
        if self.species.lower() == "christmas":
            base_price *= 3
        
        total = (1 + self.tax) * self.qty * base_price

        #if subclass is InternationalMelon:
        # and order is under

        return total


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder,self).__init__(species,qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder,self).__init__(species,qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
