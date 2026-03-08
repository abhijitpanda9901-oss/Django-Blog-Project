from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('post/<int:id>/', views.post_detail),
    path('create/', views.create_post),
]