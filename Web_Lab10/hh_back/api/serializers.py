from rest_framework import serializers


from .models import Company, Vacancy


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField(max_length=200)
    address = serializers.CharField()

    def create(self, validated_data):
        category = Company.objects.create(name=validated_data.get('name'),
                                          description=validated_data.get('description'),
                                          city=validated_data.get('city'),
                                          address=validated_data.get('address'))
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')

        instance.save()
        return instance


class CompanySerializer2(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address')
        # read_only_fields = ('name',)

class VacancySerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    # company = CompanySerializer2()
    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company')
        # read_only_fields = ('name',)

