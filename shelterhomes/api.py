from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from shelterhomes.models import ShelterHome
from shelterhomes.serializers import ShelterHomeSerializer


class ShelterHomeViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    serializer_class = ShelterHomeSerializer
    queryset = ShelterHome.objects.all()
    lookup_field = 'id'
