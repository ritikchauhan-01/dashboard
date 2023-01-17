from rest_framework import serializers
from .models import User

class RegisterationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True,)
    class Meta:
        model = User
        fields = ['username','password','first_name', 'last_name','employee_type', 'salary']
        
        def create(self, validated_data):
            return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","first_name","last_name","employee_type","salary",
        "last_login","date_joined"]






