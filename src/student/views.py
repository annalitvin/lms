from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, TemplateView

from app.mixins import CustomLoginRequiredMixin
from student.forms import StudentAddForm, StudentEditForm
from .models import Student


class IndexView(TemplateView):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Generate students in database using url: <strong> generate?student_number=1 </strong> <br>"
                            + "where <strong>student_number</strong> is number of students. <br>Default: 100 students",
                            status=200)


class GenerateStudentsView(TemplateView):

    def gen_student(self, request):

        STUDENT_NUMBER = 100

        student_number = str(request.GET.get('student_number', STUDENT_NUMBER))
        if student_number.isdigit():
            try:
                for _ in range(int(student_number)):
                    Student.generate_student()
            except Exception as ex:
                return HttpResponse(f'Data added fail! {ex}', status=500)
            return redirect('student:data_success')
        return HttpResponse("Error. The value must be numeric and greater than zero.", status=400)

    def get(self, request, *args, **kwargs):
        return self.gen_student(request)


class DataSuccessView(TemplateView):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Data added successfully! <br> <a href='/student'>Main</a>", status=200)


class StudentsListViewOne(CustomLoginRequiredMixin, ListView):
    model = Student
    template_name = 'student/students_list_one.html'
    context_object_name = 'students_list'

    paginate_by = 10

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        qs = qs.select_related('group').order_by('-id')

        if request.GET.get('fname'):
            qs = qs.filter(first_name=request.GET.get('fname'))
        if request.GET.get('lname'):
            qs = qs.filter(last_name=request.GET.get('lname'))
        if request.GET.get('mail'):
            qs = qs.filter(email=request.GET.get('mail'))

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        param = self.request.GET

        context['title'] = 'Student list 1'
        context['query_params'] = urlencode({k: v for k, v in param.items() if k != 'page'})
        return context


class StudentsListViewTwo(CustomLoginRequiredMixin, ListView):
    model = Student
    template_name = 'student/students_list_two.html'
    context_object_name = 'students_list'

    paginate_by = 10

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        qs = qs.select_related('group').order_by('-id')

        first_name, last_name, email = request.GET.get("fname"), request.GET.get("lname"), request.GET.get("mail")

        if first_name or last_name or email:
            qs = qs.filter(Q(first_name=first_name) |
                           Q(last_name=last_name) |
                           Q(email=email))
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Student list 2'
        return context


class StudentUpdateView(SuccessMessageMixin, CustomLoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'student/students_edit.html'
    form_class = StudentEditForm

    success_message = "Student has been updated!"

    def get_success_url(self):
        return reverse('student:list_one')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit student'
        return context


class StudentCreateView(CustomLoginRequiredMixin, CreateView):
    model = Student
    template_name = 'student/students_add.html'
    form_class = StudentAddForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add student'
        return context

    def get_success_url(self):
        return reverse('student:list_one')


class StudentDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Student

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, f'Student deleted!')
        return reverse('student:list_one')
