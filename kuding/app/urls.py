from django.urls import path
from . import views
from .views import post_result

app_name = 'app'

urlpatterns = [
            path('', views.index, name ='index'),
            path('viewer/', views.pdf_view, name ='pdf_view'),
            # path('result/', views.result, name = 'result'),
            path('request', views.post_result, name='post_result')
]

