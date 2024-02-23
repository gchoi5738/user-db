from django.db import models
from enum import Enum
from django.contrib.auth.hashers import make_password, check_password
from django.db.models.signals import pre_save
from django.dispatch import receiver




class OrderStatus(Enum):
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    COMPLETED = 'Completed'
    CANCELED = 'Canceled'

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=255) 
    order_status = models.CharField(
        max_length=20,
        choices=[(status.value, status.name) for status in OrderStatus],
        default=OrderStatus.PENDING.value
    )
    connected_organization = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

@receiver(pre_save, sender=User)
def custom_user_pre_save(sender, instance, **kwargs):
    # Hash the password before saving the instance
    if instance.password and not instance.password.startswith(('pbkdf2_sha256$', 'bcrypt', 'argon2')):
        instance.set_password(instance.password)