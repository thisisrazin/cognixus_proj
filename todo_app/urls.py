from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    TODOListCreateAPIView,
    TODOUpdateAPIView,
    TODODestroyAPIView
)

urlpatterns=[
    path('auth/', obtain_auth_token),
    path('todo/', TODOListCreateAPIView.as_view()),
    path('todo/update/<int:pk>', TODOUpdateAPIView.as_view()),
    path('todo/delete/<int:pk>', TODODestroyAPIView.as_view())
]
