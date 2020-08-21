from django.urls import path
from . import views

urlpatterns = [
            path('', views.index, name ='index'),
            path('viewer/', views.pdf_view, name ='pdf_view'),
]
