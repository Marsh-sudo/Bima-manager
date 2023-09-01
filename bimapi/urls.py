from django.urls import path,include
from . import views
from .views import  ClientList,ClientDetail,ClientPolicyList,PolicyDetail,AccountViewSet
from rest_framework import routers


urlpatterns = [
    path('', ClientList.as_view()),
    # path('<int:pk>/', PolicyDetail.as_view()),
    path('client/<int:pk>',ClientDetail.as_view()),
    path('client/<int:pk>/policies',ClientPolicyList.as_view()),
    path('client/<int:pk>/policies/<policy_id>',AccountViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})),

    
]