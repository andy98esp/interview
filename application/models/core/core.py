from django.db import models


class CoreModel(models.Model):
    """ A base model for all models in the application

    fields:
        instance_created_at: The date and time the instance was created.
        instance_updated_at: The date and time the instance was last updated.

        instance_is_active: A boolean indicating whether the instance is active.
    """

    instance_created_at = models.DateTimeField(auto_now_add=True)
    instance_updated_at = models.DateTimeField(auto_now=True)

    instance_is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

        # This ensures that the model is inside the application
        # All models should inherit from this class
        # Otherwise, the models won't be registered
        app_label = 'application'
