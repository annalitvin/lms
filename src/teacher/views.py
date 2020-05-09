from django.db.models import Q
from django.http import HttpResponse, Http404, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from teacher.forms import TeacherAddForm
from .models import Teacher


def index(request):

    id_teacher = request.GET.get('id')
    if id_teacher is not None:
        if not id_teacher.isdigit():
            return HttpResponse("'id' must be numeric and greatest when zero")

        id_teacher = int(id_teacher)
        if id_teacher == 0:
            return HttpResponse("'id' must be greatest when zero")

        try:
            teacher = Teacher.objects.get(pk=id_teacher)
        except Teacher.DoesNotExist:
            return HttpResponse("Generate teachers in database using url: <strong>gen_teacher?teach_number=1</strong>" +
                                "<br>" +
                                "where <strong>teach_number</strong> is number of teachers. <br>Default: 100 teachers",
                                status=200)
        return render(request, "teacher/index.html", context={"teacher": teacher})
    return HttpResponse("Введите параметр id: ?id=n")


def gen_teacher(request):

    TEACHER_NUMBER = 100

    teacher_number = request.GET.get('teach_number', TEACHER_NUMBER)
    if teacher_number.isdigit():
        try:
            for _ in range(int(teacher_number)):
                Teacher.generate_teacher()
        except Exception as ex:
            return HttpResponse(f'Data added fail! {ex}', status=500)
        return redirect('data_success')
    return HttpResponse("Error. The value must be numeric and greater than zero.", status=400)


def data_success(request):
    return HttpResponse("Data added successfully! <br> <a href='/teacher'>На главную</a>", status=200)


def teachers_list(request):
    qs = Teacher.objects.all()

    if request.GET.get('fname'):
        qs = qs.filter(first_name=request.GET.get('fname'))
    if request.GET.get('lname'):
        qs = qs.filter(last_name=request.GET.get('lname'))
    if request.GET.get('mail'):
        qs = qs.filter(email=request.GET.get('mail'))

    result = '<br>'.join(str(teacher) for teacher in qs)
    return render(request, 'teacher/teachers_list.html', {'teachers_list': result})


def add_teacher(request):

    add_teacher_template = 'teacher/add_teacher.html'

    if request.method == 'POST':
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number').strip()
            email = form.cleaned_data.get('email').strip()

            is_teacher_exists = Teacher.objects.filter(Q(phone_number=phone_number) |
                                                       Q(email=email)).exists()
            if is_teacher_exists:
                error_massage = "Teacher not added. Teacher with such phone_number and email is exists! Try again:"
                return render(request, add_teacher_template, {'form': form, "error_massage": error_massage},
                              status=400)

            form.save()
            return HttpResponseRedirect(reverse('teachers_list'))
    else:
        form = TeacherAddForm()
    return render(request, add_teacher_template, {'form': form})
