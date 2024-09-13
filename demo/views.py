import stripe
from django.shortcuts import render, redirect # type: ignore
from django.conf import settings # type: ignore

def home(request):
    return render(request, 'home.html')

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=[
            'card'
        ],
        line_items=[
            {
                'price': 'price_1PyXg6BOyGFvN7ZKL5bf4UCz',
                'quantity': 1,
            },
        ],
        mode='subscription',
        success_url='http://localhost:8000',
        cancel_url='http://localhost:8000',
    )
    return redirect(checkout_session.url, code=303)
