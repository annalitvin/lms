from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gen_student', views.gen_student, name='gen_student'),
    path('data_success', views.data_success, name='data_success'),
    path('students_list/1', views.students_list_one, name='students_list_one'),
    path('students_list/2', views.students_list_two, name='students_list_two'),
]
