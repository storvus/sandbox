import stripe
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from sandbox.settings import STRIPE_SECRET_KEY, STRIPE_PUBLISHABLE_KEY


@method_decorator(login_required, name="dispatch")
class CheckoutView(TemplateView):
    template_name = "strip/checkout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["customers"] = stripe.Customer.create(
        #     api_key=STRIPE_SECRET_KEY,
        #     idempotency_key=str(self.request.user.id + 1),
        #     email=self.request.user.email,
        #     metadata={
        #         "username": self.request.user.username,
        #         "email": self.request.user.email,
        #     }
        # )
        context["customers"] = stripe.Customer.retrieve("cus_Nz2N75oQN7wLQG", api_key=STRIPE_SECRET_KEY)
        return context


@method_decorator(login_required, name="dispatch")
class CompletedPayment(TemplateView):
    template_name = "strip/completed-payment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["customers"] = stripe.Customer.create(
        #     api_key=STRIPE_SECRET_KEY,
        #     idempotency_key=str(self.request.user.id + 1),
        #     email=self.request.user.email,
        #     metadata={
        #         "username": self.request.user.username,
        #         "email": self.request.user.email,
        #     }
        # )
        context["customers"] = stripe.Customer.retrieve("cus_Nz2N75oQN7wLQG", api_key=STRIPE_SECRET_KEY)
        return context


@login_required
def stripe_config(request):
    return JsonResponse({"stripePublishKey": STRIPE_PUBLISHABLE_KEY})


@csrf_exempt
def webhooks(request):
    webhook_secret = "whsec_37b623982f7901934dc118fe86adb6fc8969a62fc62b7b9d9369eaa087f93c1b"
    event = stripe.Webhook.construct_event(
        request.body,
        request.headers.get("stripe-signature"),
        secret=webhook_secret
    )
    return JsonResponse({"ok": "1"})


@login_required
def create_payment_intent(request):
    payment_intent = stripe.PaymentIntent.create(
        api_key=STRIPE_SECRET_KEY,
        amount=1000,
        currency="usd",
        customer="cus_Nz2N75oQN7wLQG",
        metadata={
            "order": 1,
            "user": request.user.id,
        }
    )
    print(payment_intent)
    return JsonResponse({"clientSecret": payment_intent.client_secret})


