from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView

from teacher.forms import TeacherAddForm, TeacherEditForm
from teacher.mixins import TeacherValidFormMixin
from .models import Teacher


class IndexTeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher/index.html'
    context_object_name = 'teacher'

    def get_object(self, queryset=None):

        request = self.request

        id_teacher = request.GET.get('id')
        try:
            group_obj = self.model.objects.get(pk=id_teacher)
        except self.model.DoesNotExist:
            raise Http404("Group does not exist! "
                          "Generate teachers in database using url: generate?teach_number=1" +
                          "where teach_number is number of teachers. Default: 100 teachers")
        return group_obj

    def get(self, request, *args, **kwargs):

        id_teacher = request.GET.get('id')
        if id_teacher is None:
            return HttpResponse("Введите параметр id: ?id=n")

        if id_teacher is not None:
            if not id_teacher.isdigit():
                return HttpResponse("'id' must be numeric and greatest when zero")

            id_teacher = int(id_teacher)
            if id_teacher == 0:
                return HttpResponse("'id' must be greatest when zero")

        self.object = self.get_object()
        context = self.get_context_data()
        return self.render_to_response(context)


class GenerateTeacherView(TemplateView):

    def gen_teacher(self, request):

        TEACHER_NUMBER = 100

        teacher_number = str(request.GET.get('teach_number', TEACHER_NUMBER))
        if teacher_number.isdigit():
            try:
                for _ in range(int(teacher_number)):
                    Teacher.generate_teacher()
            except Exception as ex:
                return HttpResponse(f'Data added fail! {ex}', status=500)
            return redirect('teacher:data_success')
        return HttpResponse("Error. The value must be numeric and greater than zero.", status=400)

    def get(self, request, *args, **kwargs):
        return self.gen_teacher(request)


class DataSuccessView(TemplateView):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Data added successfully! <br> <a href='/teacher'>На главную</a>", status=200)


class TeachersListView(ListView):
    model = Teacher
    template_name = 'teacher/teachers_list.html'
    context_object_name = 'teachers_list'

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        qs = qs.order_by('-id')

        if request.GET.get('fname'):
            qs = qs.filter(first_name=request.GET.get('fname'))
        if request.GET.get('lname'):
            qs = qs.filter(last_name=request.GET.get('lname'))
        if request.GET.get('mail'):
            qs = qs.filter(email=request.GET.get('mail'))

        return qs


class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teacher/edit_teacher.html'
    form_class = TeacherEditForm

    def get_success_url(self):
        return reverse('teacher:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit teacher'
        if self.object:
            context['teacher'] = self.object
        return context


class TeacherCreateView(TeacherValidFormMixin, CreateView):
    model = Teacher
    template_name = 'teacher/add_teacher.html'
    form_class = TeacherAddForm

    def get_success_url(self):
        return reverse('teacher:list')


class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teacher:list')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
