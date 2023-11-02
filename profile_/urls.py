from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from drf_yasg import openapi
from . import views


urlpatterns = [
    path('api/profile/',views.ProfileList.as_view(),),
]

