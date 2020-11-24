from rest_framework import serializers
from django.contrib.auth.models import User

class UsarioSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validate_data):
        instancia = User()
        instancia.first_name = validate_data.get('first_name')
        instancia.last_name = validate_data.get('last_name')
        instancia.username = validate_data.get('username')
        instancia.email = validate_data.get('email')
        instancia.set_password(validate_data.get('password'))
        instancia.save()
        return instancia

    def Validacion_Username(self, data):
        users = User.objects.filter(username = data)
        if len(users) != 0:
            raise serializers.ValidationError("Error: El nombre de usuario ingresado ya existe, por favor ingrese uno nuevo")
        else:
            return data
        
        