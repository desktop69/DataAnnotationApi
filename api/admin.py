from django.contrib import admin
from .models import Label, Document, Annotation
# Register your models here.
admin.site.register(Label)
admin.site.register(Document)
admin.site.register(Annotation)
