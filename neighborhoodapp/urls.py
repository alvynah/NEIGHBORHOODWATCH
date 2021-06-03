from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('api/neighbors/', views.NeighborhoodList.as_view(), name='neighbor'),
    path('api/business/', views.BusinessList.as_view(), name='business'),
    path('api/users/', views.UserList.as_view(), name='users'),
    path('api/update/users/<int:pk>/',views.UserList.as_view(), name='update_users'),
    path('api/delete/users/<int:pk>/',views.UserList.as_view(), name='delete_users'),
    path('api/update/business/<int:pk>/',views.BusinessList.as_view(), name='update_business'),
    path('api/delete/business/<int:pk>/',views.BusinessList.as_view(), name='delete_business'),
    path('api/update/neighbors/<int:pk>/',views.NeighborhoodList.as_view(), name='update_neighbors'),
    path('api/delete/neighbors/<int:pk>/',views.NeighborhoodList.as_view(), name='delete_neighbors'),
]
