from django.db.models import Q
from django.http import HttpResponse, Http404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from group.forms import GroupAddForm, GroupEditForm
from .models import Group


class IndexGroupDetailView(DetailView):
    model = Group
    template_name = 'group/index.html'
    context_object_name = 'group'

    def get_object(self, queryset=None):

        id_group = self.kwargs.get(self.pk_url_kwarg)
        try:
            group_obj = self.model.objects.get(pk=id_group)
        except self.model.DoesNotExist:
            raise Http404("Group does not exist")
        return group_obj

    def get(self, request, *args, **kwargs):

        id_group = self.kwargs.get(self.pk_url_kwarg)
        if id_group is not None:
            if id_group == 0:
                return HttpResponse("'id' must be greatest when zero")

        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Group'
        return context


class GroupListView(ListView):
    model = Group
    template_name = 'group/groups_list.html'
    context_object_name = 'groups_list'

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        qs = qs.order_by('-id')

        name = request.GET.get('name')
        specialty = request.GET.get('specialty')
        course_name = request.GET.get('course_name')

        groups_filter = Q()

        if name:
            groups_filter |= Q(name=name)
        if specialty:
            groups_filter |= Q(specialty=specialty)
        if course_name:
            groups_filter |= Q(course_name=course_name)

        qs = qs.filter(groups_filter)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Group list'
        return context


class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'group/group_edit.html'
    form_class = GroupEditForm

    def get_success_url(self):
        return reverse('group:groups_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit group'
        if self.object:
            context['group'] = self.object
        return context


class GroupCreateView(CreateView):
    model = Group
    template_name = 'group/add_group.html'
    form_class = GroupAddForm

    def get_success_url(self):
        return reverse('group:groups_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add group'
        return context


class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('group:groups_list')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
