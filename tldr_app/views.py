from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import UserSerializer, QuerySerializer
from .renderers import CustomJSONRenderer
from .services import *

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('id')
#     serializer_class = UserSerializer
#     renderer_classes = [CustomJSONRenderer]
    
# class QueryViewSet(viewsets.ModelViewSet):
#     queryset = Query.objects.all().order_by('id')
#     serializer_class = QuerySerializer
#     renderer_classes = [CustomJSONRenderer]

class UserApiView(APIView):
    renderer_classes = [CustomJSONRenderer]
    
    def get(self, request, *args, **kwargs):
      users = User.objects.all()
      serializer = UserSerializer(users, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
      serializer = UserSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	      

class QueryApiView(APIView):
    renderer_classes = [CustomJSONRenderer]
    
    def get(self, request, *args, **kwargs):
      queries = Query.objects.all()
      serializer = QuerySerializer(queries, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
                
    def post(self, request, *args, **kwargs):
      import pdb; pdb.set_trace()
      serializer = QuerySerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)