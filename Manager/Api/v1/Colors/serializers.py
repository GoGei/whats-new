from rest_framework import serializers
from core.Colors.models import CategoryColor, PostColor


class CategoryColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryColor
        fields = (
            'id',
            'name',
            'value',
            'label',
        )


class PostColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostColor
        fields = (
            'id',
            'name',
            'value',
            'label',
        )
