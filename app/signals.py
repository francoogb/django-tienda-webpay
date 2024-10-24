# signals.py
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UsersMetadata, Carrito

@receiver(pre_delete, sender=User)
def delete_related_cart_items(sender, instance, **kwargs):
    try:
        users_metadata = UsersMetadata.objects.get(user=instance)
        users_metadata.carrito_set.all().delete()
    except UsersMetadata.DoesNotExist:
        # Handle the case where UsersMetadata does not exist for the user
        pass
