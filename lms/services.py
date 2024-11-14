import stripe
from config import settings

stripe.api_key = settings.STRIPE_API_KEY

"""Создание продукта"""
def stripe_create_product(name, description):

    return stripe.Product.create(
        name=name,
        description=description
    )

def stripe_create_price(usd_price, product_id):
    stripe.Price.create(
        currency="usd",
        unit_amount=usd_price,
        recurring={"interval": "month"},
        product=product_id,
    )
