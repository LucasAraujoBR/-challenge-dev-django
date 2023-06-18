from django.urls import path
from .viewsets import ResponseAPIView

urlpatterns = [
    path('get_proposal/<int:pk>/', ResponseAPIView.as_view(), name='response-detail'),
    path('response/', ResponseAPIView.as_view(), name='response-create'),
    # path('response/<str:code>/patch/', ResponseAPIView.as_view(), name='response-patch'),
]
