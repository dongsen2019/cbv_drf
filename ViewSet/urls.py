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
from ViewSet import views

from django.urls import include

urlpatterns = [
    path('book/', views.ViewSetBookView.as_view({"get": "get_all", "post": "add_object"})),
    path('book/<int:pk>', views.ViewSetBookView.as_view({"get": "get_object", "put": "update_object", "delete": "delete_object"})),
    path('publish/', views.ViewSetPublishView.as_view({"get": "list", "post": "create"})),
    path('publish/<int:pk>', views.ViewSetPublishView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    # path('author/', views.ViewSetAuthorView.as_view()),
    # path('author/<int:pk>', views.ViewSetAuthorDetailView.as_view()),
]

