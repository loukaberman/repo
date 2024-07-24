# portfolio.py
class Portfolio:
    def __init__(self):
        self.holdings = {}

    def add_stock(self, symbol, quantity, purchase_price):
        if symbol in self.holdings:
            self.holdings[symbol]['quantity'] += quantity
            # Average purchase price
            total_cost = self.holdings[symbol]['quantity'] * self.holdings[symbol]['purchase_price'] + quantity * purchase_price
            self.holdings[symbol]['purchase_price'] = total_cost / (self.holdings[symbol]['quantity'] + quantity)
        else:
            self.holdings[symbol] = {
                'quantity': quantity,
                'purchase_price': purchase_price
            }

    def remove_stock(self, symbol, quantity):
        if symbol in self.holdings and self.holdings[symbol]['quantity'] >= quantity:
            self.holdings[symbol]['quantity'] -= quan
