from .models import Comment
from rest_framework import generics
from .serializers import CommentSerializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated 
from .permissions import IsOwnerOrReadOnly


class CommentAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CommentAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, )