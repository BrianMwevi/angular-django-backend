from django.shortcuts import render
from api.serializers import BusinessSerializer
from rest_framework import viewsets
from api.models import Business

# Create your views here.


class BusinessViewset(viewsets.ModelViewSet):
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()


# functional views 
# generics 
# viewsets - perform almost all CRUD operations
# class-based views
