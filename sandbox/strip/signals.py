import stripe
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from sandbox.settings import STRIPE_SECRET_KEY
from sandbox.strip.models import Customer


@receiver(post_save, sender=User)
def customer_create(sender, **kwargs):
    if kwargs["created"] or not hasattr(kwargs["instance"], "customer"):
        customer = stripe.Customer.create(
            api_key=STRIPE_SECRET_KEY,
            idempotency_key=str(kwargs["instance"].id),
            email=kwargs["instance"].email,
            metadata={
                "username": kwargs["instance"].username,
                "email": kwargs["instance"].email,
            }
        )
        Customer.objects.create(user=kwargs["instance"], customer_id=customer.id)

