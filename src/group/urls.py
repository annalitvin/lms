from django.urls import path

from . import views

app_name = 'group'

urlpatterns = [
    path('<int:pk>', views.IndexGroupDetailView.as_view(), name='index'),
    path('add', views.GroupCreateView.as_view(), name='add'),
    path('groups_list', views.GroupListView.as_view(), name='groups_list'),
    path('edit/<int:pk>', views.GroupUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', views.GroupDeleteView.as_view(), name='delete'),

]
