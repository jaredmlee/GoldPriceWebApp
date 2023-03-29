from django.urls import path

from . import views

app_name = 'calculator'
urlpatterns = [
    path('', views.index, name='gold'),
    path('index', views.index, name='index'),
    path('plan', views.plan, name='plan')
]
