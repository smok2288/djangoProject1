from rest_framework import serializers

from cars.models import Cars, Factory, Production, Buyer, TechPasport


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('model', 'age', 'valume', 'hspeed', 'cost')

class FactorySerializer(serializers.ModelSerializer):
    cars = serializers.SlugRelatedField(slug_field='model', read_only=True, many=True)
    class Meta:
        model = Factory
        fields = ('title', 'cars', 'country', 'city', 'street')


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = '__all__'
        depth = 2

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ('surname', 'tel', 'name')
        depth = 1


class TechPasportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechPasport
        fields = '__all__'
        depth = 1





