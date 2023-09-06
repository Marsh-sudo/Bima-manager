from django.shortcuts import render
from rest_framework import generics,permissions,viewsets
from .serializers import ClientSerializer,PolicySerializer
from .models import Client,Reminder,Policy
from .permissions import IsAuthorOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters

# Create your views here.
class ClientList(generics.ListCreateAPIView): 
    queryset = Client.objects.all() 
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'email']

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticated,)

# class PolicyDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)  # new 
#     queryset = Policy.objects.all()
#     serializer_class = PolicySerializer


class ClientPolicyList(generics.ListCreateAPIView):
    serializer_class = PolicySerializer
    permission_classes = (permissions.IsAuthenticated,)
   

    def get_queryset(self):
        client_pk = self.kwargs.get('pk')
        print(self.kwargs)
        queryset = Policy.objects.filter(client__id=client_pk)
        print(queryset.count())
        return queryset
    
    

  

# class PolicyDetail(generics.RetrieveUpdateAPIView):
#     serializer_class = PolicySerializer
#     permission_classes = (IsAuthorOrReadOnly,)
#     lookup_url_kwarg = "policy_id"

#     queryset=Policy.objects

    # def get_queryset(self):
    #     client_pk = self.kwargs.get('policy_id')
    #     print(self.allowed_methods)
    #     return Policy.objects.filter(pk=client_pk)

    # @action(detail=True, methods=['GET'], url_path='policy/(?P<policy_pk>\d+)')
    # def single_policy(self, request, client_id, policy_pk):
    #     policy = Policy.objects.get(client_id=client_id, pk=policy_pk)
    #     serializer = PolicySerializer(policy)
    #     return Response(serializer.data)

class PolicyDetailViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing single policies owned by a client.
    """
    serializer_class = PolicySerializer
    lookup_url_kwarg = "policy_id"
    queryset=Policy.objects


class SearchApiView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'email']