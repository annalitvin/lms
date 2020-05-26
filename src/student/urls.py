from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),
    path('generate', views.gen_student, name='generate'),
    path('data_success', views.data_success, name='data_success'),
    path('list/1', views.students_list_one, name='list_one'),
    path('list/2', views.students_list_two, name='list_two'),
    path('add/', views.students_add, name='add'),
    path('edit/<int:id>', views.student_edit, name='edit'),
    path('delete/<int:id>', views.student_delete, name='delete')
]
