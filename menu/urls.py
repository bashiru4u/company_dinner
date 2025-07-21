from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('food/<int:pk>/', views.food_detail, name='food_detail'),
    path('vote/<int:pk>/', views.cast_vote, name='cast_vote'),
]