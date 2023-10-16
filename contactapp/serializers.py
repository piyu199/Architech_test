from rest_framework import serializers
from .models import ContactManager

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactManager
        fields='__all__'



