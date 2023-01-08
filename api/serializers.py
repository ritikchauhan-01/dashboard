from rest_framework import serializers
from .models import User

class RegisterationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','password','first_name', 'last_name','department', 'salary', 'phone_number',]
        extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data):
            user = User.objects.create(
                username = validated_data['username'],
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],
                department = validated_data['department'],
                salary = validated_data['salary'],
                phone_number = validated_data['phone_number'],
            )
            user.set_password(validated_data['password'])
            user.save()

            return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","first_name","last_name","department","salary",
        "last_login","date_joined"]






