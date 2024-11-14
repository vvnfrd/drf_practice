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

    return stripe.Price.create(
        currency="usd",
        unit_amount=usd_price,
        recurring={"interval": "month"},
        product=product_id,
    )

def stripe_pay_session(price_id):
    return stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": price_id, "quantity": 2}],
        mode="subscription",
    )
