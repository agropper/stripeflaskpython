import os
from flask import Flask, render_template, request
import stripe

stripe_keys = {
  'secret_key': "rk_test_51DoMk3Jy4KVxLLXghZxa18FRkCK4aDV8GcoLPr2xNG8eZtTBKfE1sAQ0l4twqvPd8f5rONTu1yaTQbgHZNowNgYL00RsxL1f15",
  'publishable_key': "pk_test_n4B7NQ3lBzJ6OHs8l9VsBWLm"
}

stripe.api_key = stripe_keys['secret_key']

print(stripe.Plan.list())

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', key=stripe_keys['publishable_key'])

@app.route('/charge', methods=['POST'])
def charge():
  amount = 500

  customer = stripe.Customer.create(
      email='customer@example.com',
      card=request.form['stripeToken']
  )

  charge = stripe.Charge.create(
      customer=customer.id,
      amount=amount,
      currency='usd',
      description='Flask Charge'
  )

  return render_template('charge.html', amount=amount)

if __name__ == '__main__':
  app.run(debug=True)
