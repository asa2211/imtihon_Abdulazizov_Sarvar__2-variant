from rest_framework import serializers
from .models import OrderModel, UstaModel


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'


class UstaSerializers(serializers.ModelSerializer):
    class Meta:
        model = UstaModel
        fields = '__all__'