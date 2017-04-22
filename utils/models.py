import uuid

from django.db import models


class BaseModel(models.Model):
    """
    This will add the basic fields to the model
    """

    class Meta:
        abstract = True

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)