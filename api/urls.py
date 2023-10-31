from django.urls import path
from .views import LabelList, LabelDetails

urlpatterns = [
    path('label/', LabelList.as_view()),
    path('label/<int:pk>/', LabelDetails.as_view()),

]
