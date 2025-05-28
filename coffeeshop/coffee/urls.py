from django.urls import path
from . import views 


urlpatterns = [
    path('', views.coffee_list, name='coffee_list'),
    path('create/', views.coffee_create, name='coffee_create'),
    path('update/<int:pk>/', views.coffee_update, name='coffee_update'),
    path('delete/<int:pk>/', views.coffee_delete, name='coffee_delete'),
]   

