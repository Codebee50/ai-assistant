from functools import reduce


items_prices = {
    "hat": {"original_price": 20, "discount": 0},
    "scarf": {"original_price": 25, "discount": 10},
    "sunglasses": {"original_price": 50, "discount": 15},
    "belt": {"original_price": 30, "discount": 0},
    "gloves": {"original_price": 18, "discount": 5},
    "watch": {"original_price": 120, "discount": 20},
    "bracelet": {"original_price": 45, "discount": 0},
    "necklace": {"original_price": 70, "discount": 25},
    "earrings": {"original_price": 35, "discount": 0},
    "beanie": {"original_price": 22, "discount": 10},
    "tie": {"original_price": 28, "discount": 0},
    "wallet": {"original_price": 60, "discount": 15},
    "anklet": {"original_price": 16, "discount": 5},
    "socks": {"original_price": 12, "discount": 0},
    "cufflinks": {"original_price": 40, "discount": 10},
    "keychain": {"original_price": 10, "discount": 0},
    "backpack": {"original_price": 80, "discount": 20},
    "handbag": {"original_price": 150, "discount": 30},
    "brooch": {"original_price": 38, "discount": 0},
    "suspenders": {"original_price": 26, "discount": 10},
    "visor": {"original_price": 18, "discount": 0},
}



def get_discounted_price(product):
    print(f'Getting discounted price for {product}')
    
    if product['discount'] > 0:
        discounted_price = round(product["original_price"] * (1- product["discount"]/100), 2)
        return discounted_price
    else:
        return product['original_price']

def get_item_price(product_name:str):
    print("Getting item price for", product_name)
    product = items_prices.get(product_name.lower())

    if not product:
        return "Unknown"

    return product.get('original_price')


def get_product_discount(product_name):
    print('Getting product discount for', product_name)
    product= items_prices.get(product_name.lower())
    
    if not product:
        return "Unknown"
    
    return product.get('discount')

def get_product_names():
    print("Fetching all products")
    return items_prices
    # return list(items_prices.keys())


def checkout_products(product_names: list):
    order_total = 0
    for product_name in product_names:
        product = items_prices.get(product_name)
        if product:
            price = get_discounted_price(product)
            order_total += price
    
    #create a fake payment url
    return "https://kyrian.pro?uid=cd6094aa-de01-4594-8d37-14d18637d78c", order_total
        