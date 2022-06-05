from . import views
from django.urls import path

app_name = "book"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('create/', views.create, name="create")
]