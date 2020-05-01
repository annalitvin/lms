from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import Student


def index(request):
    return HttpResponse("Generate students in database using url: <strong> gen_student?student_number=1 </strong> <br>"
                        + "where <strong>student_number</strong> is number of students. <br>Default: 100 students",
                        status=200)


def gen_student(request):

    STUDENT_NUMBER = 100

    student_number = request.GET.get('student_number', STUDENT_NUMBER)
    if student_number.isdigit():
        try:
            for _ in range(int(student_number)):
                Student.generate_student()
        except Exception as ex:
            return HttpResponse(f'Data added fail! {ex}', status=500)
        return redirect('data_success')
    return HttpResponse("Error. The value must be numeric and greater than zero.", status=400)


def data_success(request):
    return HttpResponse("Data added successfully! <br> <a href='/student'>Main</a>", status=200)
