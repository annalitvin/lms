from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gen_teacher', views.gen_teacher, name='gen_teacher'),
    path('data_success', views.data_success, name='data_success')
]