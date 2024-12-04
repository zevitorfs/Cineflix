from rest_framework import serializers

#Isso vai ser utilizado como resposta da API
class CategoryResponseSerialezer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    is_active = serializers.BooleanField()
    

class ListCategoryResponseSerializer(serializers.Serializer):
    data = CategoryResponseSerialezer(many=True)
    
#Será utilizaod para valida a requisição fora da view
class RetriverCategoryResquestSerializer(serializers.Serializer):
    id = serializers.UUIDField()
#Envelope a resposta
class RetriveCategoryResponseSerializer(serializers.Serializer):
    data = CategoryResponseSerialezer(source="*")
