import json
from django.shortcuts import get_object_or_404, render
from h11 import Response
from rest_framework import generics
from .models import Label, Document, Annotation
from .serializers import GenerateDocumentSerializer, LabelSerializer, DocumentSerializer, AnnotationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class LabelList(generics.ListCreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabelDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
# Annotations here .
class AnnotationtList(generics.ListCreateAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer

class AnnotationDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
# Document here .
class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

# file generations 

class FileGeneratorView(APIView):
    def get(self, request, id):
        document = get_object_or_404(Document, pk=id)
        serializer = GenerateDocumentSerializer(document)
        serialized_data = serializer.data  # Serialized document data with annotations
        # print(serialized_data)  # Print the serialized data in JSON format
        # Specify the file path to save the JSON file
        file_path = "C:/Users/Public/ubiai/serialized_data.json"
        with open(file_path, 'w') as file:
            file.write(json.dumps(serialized_data, separators=(',', ':')))
        return Response("Document object printed in the console", status=status.HTTP_200_OK)