from rest_framework import serializers
from .models import Label, Document, Annotation


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ('__all__')
class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ('__all__')

class DocumentSerializer(serializers.ModelSerializer):
  #  annotations = AnnotationSerializer(many=True, read_only=True)   # problem is here bro
    class Meta:
        model = Document
        fields = ('__all__')

class GenerateDocumentSerializer(serializers.ModelSerializer):
    annotations = AnnotationSerializer(many=True, read_only=True)   # problem is here bro
    class Meta:
        model = Document
        fields = ('__all__')
