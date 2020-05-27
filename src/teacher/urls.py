from django.urls import path

from . import views

app_name = 'teacher'

urlpatterns = [
    path('', views.IndexTeacherDetailView.as_view(), name='index'),
    path('generate', views.GenerateTeacherView.as_view(), name='generate'),
    path('data_success', views.DataSuccessView.as_view(), name='data_success'),
    path('list', views.TeachersListView.as_view(), name='list'),
    path('add', views.TeacherCreateView.as_view(), name='add'),
    path('edit/<int:pk>', views.TeacherUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', views.TeacherDeleteView.as_view(), name='delete')
]
