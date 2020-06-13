from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView

from app.mixins import CustomLoginRequiredMixin
from teacher.forms import TeacherAddForm, TeacherEditForm
from .models import Teacher


class IndexTeacherDetailView(CustomLoginRequiredMixin, DetailView):
    model = Teacher
    template_name = 'teacher/index.html'
    context_object_name = 'teacher'

    def get_object(self, queryset=None):

        id_teacher = self.kwargs.get(self.pk_url_kwarg)
        print(id_teacher, "erwr")
        try:
            group_obj = self.model.objects.get(pk=id_teacher)
        except self.model.DoesNotExist:
            raise Http404("Group does not exist! "
                          "Generate teachers in database using url: generate?teach_number=1" +
                          "where teach_number is number of teachers. Default: 100 teachers")
        return group_obj

    def get(self, request, *args, **kwargs):

        id_teacher = self.kwargs.get(self.pk_url_kwarg)

        if id_teacher is not None:
            if id_teacher == 0:
                return HttpResponse("'id' must be greatest when zero")

        return super().get(request, *args, **kwargs)


class GenerateTeacherView(CustomLoginRequiredMixin, TemplateView):

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
        return HttpResponse("Data added successfully! <br> <a href='/'>На главную</a>", status=200)


class TeachersListView(CustomLoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teacher/teachers_list.html'
    context_object_name = 'teachers_list'

    paginate_by = 10

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Teacher list'
        return context


class TeacherUpdateView(SuccessMessageMixin, CustomLoginRequiredMixin, UpdateView):
    model = Teacher
    template_name = 'teacher/edit_teacher.html'
    form_class = TeacherEditForm

    success_message = "Teacher has been updated"

    def get_success_url(self):
        return reverse('teacher:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit teacher'
        if self.object:
            context['teacher'] = self.object
        return context


class TeacherCreateView(CustomLoginRequiredMixin, CreateView):
    model = Teacher
    template_name = 'teacher/add_teacher.html'
    form_class = TeacherAddForm

    def get_success_url(self):
        return reverse('teacher:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add teacher'
        return context


class TeacherDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teacher:list')

    def post(self, *args, **kwargs):
        messages.success(self.request, f'Teacher deleted!')
        return super().post(*args, **kwargs)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
