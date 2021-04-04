#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, jsonify, request

import stripe
# This is your real test secret API key.
stripe.api_key = 'sk_test_QwhVPW60WK5gHKHdbbLEKwTi'
# stripe.api_key = 'pk_test_n4B7NQ3lBzJ6OHs8l9VsBWLm'

print(stripe.Plan.list(limit=1))

app = Flask(__name__,
            static_url_path='',
            static_folder='.')

YOUR_DOMAIN = 'https://stripeflaskpython-y6hf5.ondigitalocean.app'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 2000,
                        'product_data': {
                            'name': 'Stubborn Attachments',
                            'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403


if __name__ == '__main__':
    app.run(port=8080)

