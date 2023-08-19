from rest_framework import serializers
from core.Category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name_data',
            'description_data',
            'position',
            'color',
            'slug',
            'label',
        )
