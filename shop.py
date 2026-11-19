def apply_discount(price, percent):

    return price * (100 - percent) / 100
    
def add_tax(price, rate=0.2):
    
    return price * (1 + rate)

class Product:
    def __init__(self, sku, name, price):
        
        if not sku:
            raise ValueError("sku is required")
            self.sku = sku
            self.name = name
            self.price = price
def sort_by_price(products):
    return sorted(products, key=lambda p: p.price) 
def in_stock(stock, sku):
    return stock.get(sku, 0) > 0       

