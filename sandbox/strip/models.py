from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    customer_id = models.CharField(max_length=100, null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        app_label = "strip"
