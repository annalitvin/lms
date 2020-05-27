from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('generate', views.GenerateStudentsView.as_view(), name='generate'),
    path('data_success', views.DataSuccessView.as_view(), name='data_success'),
    path('list/1', views.StudentsListViewOne.as_view(), name='list_one'),
    path('list/2', views.StudentsListViewTwo.as_view(), name='list_two'),
    path('add/', views.StudentCreateView.as_view(), name='add'),
    path('edit/<int:pk>', views.StudentUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', views.StudentDeleteView.as_view(), name='delete')
]
