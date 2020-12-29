from django.urls import path
from . import views
urlpatterns = [
    path('', views.create_view, name='create_view'),
    path('retrive', views.list_view, name='list_view'),
    path('update', views.update_view, name='update_view'),
   
]

