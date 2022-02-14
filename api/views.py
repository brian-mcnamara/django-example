from django.shortcuts import render

from rest_framework import viewsets

from .serializers import NodeSerializer
from .models import Node


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all().order_by('id')
    serializer_class = NodeSerializer
