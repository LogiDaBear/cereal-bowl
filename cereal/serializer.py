from rest_framework import serializers
from .models import Cereal

class CerealSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'brand', 'rating', 'reviewer')
        model = Cereal