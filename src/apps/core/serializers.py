from rest_framework import serializers
from .models import (
    Application,
)

class ApplicationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        exclude = ("polymorphic_ctype",)

class ApplicationReadSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Application
        exclude = ("polymorphic_ctype",)

