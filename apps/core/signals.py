from .models import Application
from django.db.models.signals import (
    pre_init,   post_init,
    pre_save,   post_save,
    pre_delete, post_delete,
    m2m_changed
)
from django.dispatch import receiver
from django.contrib.auth.models import Group

## Signals from Application
@receiver(pre_init, sender=Application)
def pre_init_application(sender, *args, **kwargs):
    pass

@receiver(post_init, sender=Application)
def post_init_application(sender, instance, **kwargs):
    pass

@receiver(pre_save, sender=Application)
def pre_save_application(sender, instance, raw, using, update_fields, **kwargs):
    pass

@receiver(post_save, sender=Application)
def post_save_application(sender, instance, created, raw, using, update_fields, **kwargs):
    pass

@receiver(pre_delete, sender=Application)
def pre_delete_application(sender, instance, using, **kwargs):
    pass

@receiver(post_delete, sender=Application)
def post_delete_application(sender, instance, using, **kwargs):
    pass

@receiver(m2m_changed, sender=Application)
def m2m_changed_application(sender, instance, action, reverse, model, pk_set, using, **kwargs):
    pass

