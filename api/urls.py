from django.urls import path
from .views import FileGeneratorView, LabelList, LabelDetails , DocumentList, DocumentDetails, AnnotationtList, AnnotationDetails

urlpatterns = [
    path('label', LabelList.as_view()),
    path('label/<int:pk>', LabelDetails.as_view()),
    path('Document', DocumentList.as_view()),
    path('Document/<int:pk>', DocumentDetails.as_view()),
    path('Annotation', AnnotationtList.as_view()),
    path('Annotation/<int:pk>', AnnotationDetails.as_view()),
    path('generator/<int:id>/', FileGeneratorView.as_view()),

]
