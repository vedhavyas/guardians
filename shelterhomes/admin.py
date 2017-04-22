from django.contrib import admin

from shelterhomes.models import ShelterHomeDetails, ShelterHome


@admin.register(ShelterHomeDetails)
class ShelterHomeDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(ShelterHome)
class ShelterHomeAdmin(admin.ModelAdmin):
    pass
