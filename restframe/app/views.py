from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.models import District
from app.serializers import DistrictSerializer, UserSerializer
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def district_add(request):
    serializer = DistrictSerializer()
    if request.method == 'POST':
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getdata(request):
    data = District.objects.all()
    serializer = DistrictSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def RegisterUser(request):
    serializer = UserSerializer()
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        token_obj1, _ = Token.objects.get_or_create(user=user)
        return Response({'status': 200, 'payload': serializer.data, 'token': str(token_obj1)})


@api_view(['PUT'])
def district_update(request, id):
    try:
        instance = District.objects.get(id=id)
    except District.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = DistrictSerializer(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
