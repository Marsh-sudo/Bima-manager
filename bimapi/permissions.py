from rest_framework import permissions
from django.contrib.auth.models import User

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj) :
        #Read-Only permission is granted to anyone who can access the API endpoint.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.client == request.user