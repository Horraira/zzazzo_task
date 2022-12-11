from django.db import models
import uuid
from oscar.core.loading import get_model

Product = get_model('catalogue', 'Product')


# Create your models here.

class User(models.Model):
    # uId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=255, blank=True, null=True)
    lastName = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.lastName


class Purchase(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    purchase = models.OneToOneField(Purchase, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
