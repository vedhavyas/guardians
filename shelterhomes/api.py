from rest_framework.viewsets import ModelViewSet

from shelterhomes.models import ShelterHome
from shelterhomes.serializers import ShelterHomeSerializer


class ShelterHomeViewSet(ModelViewSet):
    serializer_class = ShelterHomeSerializer
    queryset = ShelterHome.objects.all()
    lookup_field = 'id'
