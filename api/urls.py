from django.urls import path
from .views import LabelList, LabelDetails #, DocumentList, DocumentDetails

urlpatterns = [
    path('label', LabelList.as_view()),
    path('label/<int:pk>', LabelDetails.as_view()),
    # path('Document', DocumentList.as_view()),
    # path('Document/<int:pk>', DocumentDetails.as_view())

]
