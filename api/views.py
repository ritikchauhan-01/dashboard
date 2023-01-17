import json
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from .serializers import  RegisterationSerializer, UserSerializer
from .models import User


# Register User API
@api_view(["POST"])
@permission_classes([AllowAny])
def RegisterationView(request):
    serializer = RegisterationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data,  status=status.HTTP_201_CREATED)


# Login User API
@api_view(["POST"])
@permission_classes([AllowAny])
def LoginView(request):

        data = {}
        details = request.body
        reqBody = json.loads(details)
        username = reqBody['username']
        # password = reqBody['password']
        
        try:
            Account = User.objects.get(username=username)
        except BaseException as e:
            raise ValidationError({"400": f'{str(e)}'})

        token = Token.objects.get_or_create(user=Account)[0].key

        # if not check_password(password, Account.password):
        #     raise ValidationError({"message": "Incorrect Login credentials"})

        if Account:
            if Account.is_active:
                print(request.user)
                login(request, Account)
                data["message"] = "user logged in"
                data["uesrname"] = Account.username

                Res = {"data": data, "token": token}

                return Response(Res)

            else:
                raise ValidationError({"400": f'Account not active'})

        else:
            raise ValidationError({"400": f'Account doesnt exist'})


# Logout User API
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def LogoutView(request):
    request.user.auth_token.delete()
    logout(request)

    return Response("User Logged Out Successfully")


# Get User Details API
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def UserView(request):
    serializer = UserSerializer(instance=request.user)

    return Response(serializer.data, status=status.HTTP_200_OK)

