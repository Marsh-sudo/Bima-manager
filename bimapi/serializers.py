from rest_framework import serializers 
from .models import Policy,Client,Reminder


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model= Policy
        fields = ('id','client','policy_type','policy_number','premium_amount','start_date','end_date','is_active')


class ClientSerializer(serializers.ModelSerializer):
    policies = PolicySerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = '__all__'