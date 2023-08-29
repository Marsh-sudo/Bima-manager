from django.shortcuts import render
from rest_framework import generics,permissions,viewsets
from .serializers import ClientSerializer,PolicySerializer
from .models import Client,Reminder,Policy
from .permissions import IsAuthorOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class ClientList(generics.ListCreateAPIView): 
    queryset = Client.objects.all() 
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# class PolicyDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)  # new 
#     queryset = Policy.objects.all()
#     serializer_class = PolicySerializer


class ClientPolicyList(generics.ListCreateAPIView):
    serializer_class = PolicySerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        return Policy.objects.filter(client__created_by=user)
    


class PolicyDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PolicySerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        client_pk = self.kwargs.get('client_id')
        return Policy.objects.filter(client_id=client_pk)

    @action(detail=True, methods=['GET'], url_path='policy/(?P<policy_pk>\d+)')
    def single_policy(self, request, client_id, policy_pk):
        policy = Policy.objects.get(client_id=client_id, pk=policy_pk)
        serializer = PolicySerializer(policy)
        return Response(serializer.data)