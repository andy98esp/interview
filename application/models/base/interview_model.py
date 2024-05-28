from django.db import models

from application.models.core.core import CoreModel


class InterViewModel(CoreModel):
    field1 = models.CharField(max_length=20, blank=True, null=True)
