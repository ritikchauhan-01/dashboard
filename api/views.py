from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from .serializers import  RegisterationSerializer
from django.contrib.auth import authenticate
from .models import User


@api_view(["POST"])
@permission_classes([AllowAny,])
def RegisterationView(request):
    serializer = RegisterationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,  status=status.HTTP_201_CREATED)

    return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def LogoutView(request):
    request.user.auth_token.delete()
    logout(request)

    return Response("User Logged Out Successfully")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def UserView(self, request):
    user = self.request.data
    content = self.UserSerializer(instance=user)

    return Response(content=content.data, status=status.HTTP_200_OK)







   
# @api_view(["POST"])
# @permission_classes([AllowAny])
# def LoginView(request):
#     data = {}
#     reqBody = json.loads(request.body)
#     email = reqBody['email']
#     password = reqBody['password']

#     try:
#         Account = User.objects.get(email=email)
#     except BaseException as e:
#         raise ValidationError({"400": f'{str(e)}'})
    
#     token = Token.objects.get_or_create(user=Account)[0].key
#     print(token)

#     if not check_password(password, Account.password):
#         raise ValidationError ({"message": "Incorrect Login Credentials"})

#     if Account:
#         if Account.is_active:
#             login(request, Account)
#             data["message"] = "User Logged in Successfully"
#             data["email"] = Account.email

#             context = {"data": data, "token": token}

#             return Response(context)
#         else:
#             raise ValidationError({"400": f'Account Not Active'})

#     else:
#         raise ValidationError({"400": f'Account Does Not Exist'})




