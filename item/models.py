from django.db import models
from common.models import BaseModel
from item.enum import StatusEnum


class Item(BaseModel):
    """
    Item model
    """
    title = models.CharField(help_text='Title of Item', max_length=255)

    description = models.CharField(help_text='Description of Item', max_length=500)

    status = models.CharField(
        help_text='Status of Item',
        max_length=255,
        choices=[(c, c.value) for c in StatusEnum]
    )
