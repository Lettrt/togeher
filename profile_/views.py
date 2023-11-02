
from django.shortcuts import render


from rest_framework import generics,permissions
from .serializers import ProfileSerializer
from .models import Profile

# Create your views here.





class ProfileList(generics.ListCreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
