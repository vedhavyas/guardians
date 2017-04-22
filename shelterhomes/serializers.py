from rest_framework import serializers

from shelterhomes.models import ShelterHomeDetails, ShelterHome


class ShelterHomeDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShelterHomeDetails
        fields = [
            'alternate_phone',
            'email',
            'website',
            'address',
            'latitude',
            'longitude',
            'org_type',
            'years_of_operation',
            'home_type',
            'total_children'
        ]


class ShelterHomeSerializer(serializers.ModelSerializer):

    details = ShelterHomeDetailsSerializer()

    class Meta:
        model = ShelterHome
        fields = [
            'id',
            'name',
            'phone',
            'contact_name',
            'details',
        ]

        read_only_fields = ('id',)

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        details = ShelterHomeDetails.objects.create(**details_data)
        return ShelterHome.objects.create(details=details, **validated_data)

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details')
        details_instance = instance.details
        for attr_name, value in details_data.items():
            setattr(details_instance, attr_name, value)
        details_instance.save()
        return super().update(instance, validated_data)
