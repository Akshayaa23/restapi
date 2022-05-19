from rest_framework import serializers
from .models import Drink
from django.db.models import fields

class DrinkSerializer(serializers.ModelSerializer):  
    full_name =  serializers.SerializerMethodField()
    class Meta:
       model =  Drink 
       fields = '__all__'

    def get_full_name(self, obj):
        return f'{obj.name} {obj.description}'


# class DrinkSerializer(serializers.Serializer):
#     id=serializers.IntegerField(default=1)
#     name=serializers.CharField(max_length=200)
#     description=serializers.CharField(max_length=200)

#     def create(self, validated_data):
#          return Drink.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.id = validated_data.get('id',instance.id)
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.save()
#         return instance

