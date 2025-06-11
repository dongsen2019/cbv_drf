"""
URL configuration for CBV project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GenericAPIView import views

from django.urls import include

urlpatterns = [
    path('book/', views.GenericBookView.as_view()),
    path('book/<int:pk>', views.GenericBookDetailView.as_view()),
    path('publish/', views.GenericPublishView.as_view()),
    path('publish/<int:pk>', views.GenericPublishDetailView.as_view()),
    path('author/', views.GenericAuthorView.as_view()),
    path('author/<int:pk>', views.GenericAuthorDetailView.as_view()),
    path('location/', views.GenericLocationView.as_view()),
    path('location/<int:pk>', views.GenericLocationDetailView.as_view())
]



