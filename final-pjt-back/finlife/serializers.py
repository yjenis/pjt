from rest_framework import serializers
from .models import DepositProducts,DepositOptions,SavingProducts,SavingOptions

#예금---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model= DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model= DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)

#적금---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model= SavingProducts
        fields = '__all__'

class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model= SavingOptions
        fields = '__all__'
        read_only_fields = ('product',)
