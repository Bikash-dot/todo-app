from django.urls import path,URLPattern
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('update/<str:pk>/',views.updateTask,name="update"),
    path('delete/<str:pk>/', views.deleteTask, name="delete")

]

