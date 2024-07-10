
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['POST'])
@permission_classes([AllowAny]) 
def login(request):
            
    user = None
    
    if '@' in request.data['field']:        
        user = get_object_or_404(User, email=request.data['field'])
    else:        
        user = get_object_or_404(User, username=request.data['field'])
                        
    if not user.check_password(request.data['password']):
        return Response({"error":'Contraseña incorrecta'},status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)        
    serializer = UserSerializer(user)    
    
    return Response({"token":token.key,'user':serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny]) 
def register(request):
    serializer =  UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(email=serializer.data['email'])
        user.set_password(serializer.data['password'])
        user.save()
        
        token  = Token.objects.create(user = user)
                        
        return Response({'token':token.key,'user':serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
