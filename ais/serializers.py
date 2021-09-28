from rest_framework import serializers
from .models import *

class ClientListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        exclude = ('')
#
# class ClientDetailSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Client
#         fields = ('first_name', 'last_name', 'sex', 'label')