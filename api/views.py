from django.shortcuts import render
from rest_framework import generics

from .models import Label
from .serializers import LabelSerializer
# Create your views here.

class LabelList(generics.ListCreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabelDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer