product_price_function = {
    "name": "product_price",
    "description": "Get the price of a product. Call this whenever you need to know the price of a product, for example when the customer says 'I want to buy a belt' or 'Tell me the price of a belt'",
    "parameters": {
        "type": "object",
        "properties": {
            "product_name": {
                "type": "string",
                "description": "The name of the product you want to know its price",
            }
        },
        "required": ["product_name"],
        "additionalProperties": False,
    },
}


# product_has_discount_function = {
#     "name": "product_has_discount",
#     "description": "Checks if a discount exists on a product, returns 0 if there is no discount, Unknown if the product is not found and a number greater than 0 representing the discount percentage if the product exists and has a discount, call this function whenever you need to know if there is a discount on a product",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "product_name": {
#                 "type": "string",
#                 "description": "The name of the product you want to know its price",
#             }
#         },
#         "required": ["product_name"],
#         "additionalProperties": False,
#     },
# }

available_products_function = {
    "name": "available_products",
    "description": "Get a lit of all the products that are currently available, their original prices and discounts if any, for example, a discount of 20 indicates a 20% discount on the item, Call this whenever you want to know the products we currently have available for example the user says 'I want to buy a belt'",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": [],
        "additionalProperties": False,
    },
}


validate_payment_function = {
    "name": "validate_payment",
    "description": "Validate a users payment, call this whenever the user gives you a uuid, or if they say they want to validate their payment, ask them to paste in a uuid",
    "parameters": {
        "type": "object",
        "properties": {
            "payment_reference": {
                "type": "string",
                "description": "The uuid payment reference",
            }
        },
        "required": ["payment_reference"],
        "additionalProperties": False,
    },
}


checkout_function = {
    "name": "checkout_products",
    "description": "Checkout products and get a payment url after a user have decided which products they want to buy, call this function when the user has finally decided the products they want to buy and you want to give them a payment url to make payment, after payment, they are to give you a uuid to validate their payment and process their order",
    "parameters": {
        "type": "object",
        "properties": {
            "product_names": {
                "type": "array",
                "items": {"type": "string"},
                "description": "A list of product names the user wants to buy",
            }
        },
        "required": ["product_names"],
        "additionalProperties": False,
    },
}

tools = [
    {"type": "function", "function": product_price_function},
    # {"type": "function", "function": product_has_discount_function},
    {"type": "function", "function": available_products_function},
    {"type": "function", "function": checkout_function},
    {"type": "function", "function": validate_payment_function},
]
