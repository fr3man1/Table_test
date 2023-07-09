from rest_framework import serializers
from .models import Table, Row


class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Row
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    rows = RowSerializer(many=True, read_only=True)

    class Meta:
        model = Table
        fields = '__all__'
