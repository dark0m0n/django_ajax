from django.urls import path

from ajaxsite import views

urlpatterns = [
    path('', views.index),
    path('email/', views.email),
    path('number', views.number),
]
