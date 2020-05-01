from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import Teacher


def index(request):
    return HttpResponse("Generate teachers in database using url: <strong> gen_teacher?teach_number=1 </strong> <br>" +
                        "where teach_number is number of teachers. <br>Default: 100 teachers", status=200)


def gen_teacher(request):

    TEACHER_NUMBER = 100

    teacher_number = request.GET.get('teach_number', TEACHER_NUMBER)
    if teacher_number.isdigit():
        try:
            for _ in range(int(teacher_number)):
                Teacher.generate_teacher(Teacher)
        except Exception as ex:
            return HttpResponse(f'Data added fail! {ex}', status=500)
        return redirect('data_success')
    return HttpResponse("Error. The value must be numeric and greater than zero.", status=400)


def data_success(request):
    return HttpResponse("Data added successfully! <br> <a href='/teacher'>На главную</a>", status=200)
