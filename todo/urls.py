from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('create', views.Create.as_view(), name="create"),
    path('list', views.List.as_view(), name="list"),
    path('delete/<int:pk>/', views.DeleteItem.as_view(), name="delete"),
]

