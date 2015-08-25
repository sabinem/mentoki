
from django.views.generic import FormView

import braintree




import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="use_your_merchant_id",
                                  public_key="use_your_public_key",
                                  private_key="use_your_private_key")
import braintree

braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    "7tsyzcf8cwwpq6vb",
    "qzqfmvkbjcwbf73m",
    "8888fe3713e334e3621f4360ea1c7c4f"
)
braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="7tsyzcf8cwwpq6vb",
                                  public_key="qzqfmvkbjcwbf73m",
                                  private_key="8888fe3713e334e3621f4360ea1c7c4f")

result = braintree.Transaction.sale({
    "amount": "1000.00",
    "credit_card": {
        "number": "4111111111111111",
        "expiration_date": "05/2012"
    }
})

if result.is_success:
    print("success!: " + result.transaction.id)
elif result.transaction:
    print("Error processing transaction:")
    print("  code: " + result.transaction.processor_response_code)
    print("  text: " + result.transaction.processor_response_text)
else:
    for error in result.errors.deep_errors:
        print("attribute: " + error.attribute)
        print("  code: " + error.code)
        print("  message: " + error.message)


class PaymentView(FormView):
    form_class = 'PaymentForm'
    template_name = 'payments/payments.html'

    def form_valid(self, form):
        pass

@app.route("/client_token", methods=["GET"])
def client_token():
  return braintree.ClientToken.generate()