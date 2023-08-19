from rest_framework import serializers
from core.Colors.models import CategoryColor


class CategoryColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryColor
        fields = (
            'id',
            'name',
            'value',
            'label',
        )
