from rest_framework.serializers import ModelSerializer
from .models import Bigreview


class BigreviewSerializer(ModelSerializer):
    class Meta:
        model = Bigreview
        fields = "__all__"
