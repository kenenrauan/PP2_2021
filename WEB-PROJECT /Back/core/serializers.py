from rest_framework import serializers
from core.models import *
from django.contrib.auth.models import User


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField()
    image = serializers.CharField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        product = Product.objects.create(name=validated_data.get('name'),
                                         description=validated_data.get('description'),
                                         image=validated_data.get('image'),
                                         price=validated_data.get('price'))
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class ProductSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class OrderSerializer2(serializers.ModelSerializer):
    #
    class Meta:
        model = Order
        fields = ('id', 'customer', 'product',  'date_created', 'status', 'note')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']

