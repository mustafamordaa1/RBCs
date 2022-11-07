from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('<int:year>/<str:subject>', views.lectures)
]