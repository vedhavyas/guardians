from django.db import models
from djchoices.choices import DjangoChoices, ChoiceItem

from utils.models import BaseModel


class ShelterHomeDetails(BaseModel):

    class Meta:
        verbose_name = "Shelter Home Details"
        verbose_name_plural = "Shelter Homes Details"

    class ORGType(DjangoChoices):
        Trust = ChoiceItem(1, "Trust")
        Society = ChoiceItem(2, "Society")
        Other = ChoiceItem(3, "Other")

    class HomeType(DjangoChoices):
        Boys = ChoiceItem(1, "Boys")
        Girls = ChoiceItem(2, "Girls")
        Both = ChoiceItem(3, "Boys & Girls")

    alternate_phone = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text='Alternate contact number'
    )

    email = models.EmailField(null=True, blank=True)

    website = models.URLField(null=True, blank=True)

    address = models.TextField(null=True, blank=True)

    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    org_type = models.PositiveSmallIntegerField(choices=ORGType.choices, default=ORGType.Other)

    years_of_operation = models.PositiveIntegerField(null=True, blank=True)

    home_type = models.PositiveSmallIntegerField(choices=HomeType.choices, null=True, blank=True)

    total_children = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        if hasattr(self, 'shelterhome'):
            return "{}'s details".format(self.shelterhome.name)

        return super().__str__()


class ShelterHome(BaseModel):
    name = models.CharField(
        unique=True,
        help_text='Name of the Shelter Home.',
        max_length=50
    )

    phone = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text='Primary contact number.'
    )

    contact_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        help_text='Primary contact name'
    )

    details = models.OneToOneField(ShelterHomeDetails)

    def __str__(self):
        return self.name
