from django.db import models
from django.utils.translation import gettext_lazy as _
from polymorphic.models import PolymorphicModel


class Application(PolymorphicModel, models.Model):
    """"""

    github = models.CharField(max_length=300, null=True, blank=True)
    repository = models.CharField(max_length=300, null=True, blank=True)



    class Meta:
        db_table = 'application'

