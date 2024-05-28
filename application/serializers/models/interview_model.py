from rest_framework import serializers

from application.models import InterViewModel


class InterViewModelSerializer(serializers.ModelSerializer):
    field1 = serializers.CharField(max_length=20, allow_blank=True, allow_null=False)

    class Meta:
        model = InterViewModel
        fields = ['field1', ]
