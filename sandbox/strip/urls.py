from django.urls import path

from sandbox.strip.views import CheckoutView, stripe_config, create_payment_intent, webhooks, CompletedPayment

app_name = "strip"

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name="checkout"),
    path('config/', stripe_config, name="stripe_config"),
    path('create-payment-intent/', create_payment_intent, name="create_payment_intent"),
    path('webhooks/', webhooks, name="webhooks"),
    path('completed-payment/', CompletedPayment.as_view(), name="completed_payment"),
]
