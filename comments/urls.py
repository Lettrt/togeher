from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/comment/', views.CommentAPIView.as_view()),
    path('api/v1/comment/<int:pk>/', views.CommentAPIUpdateDestroy.as_view()),
]