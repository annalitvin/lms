from django.db.models import Q
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


def students_list_one(request):
    qs = Student.objects.all()

    if request.GET.get('fname'):
        qs = qs.filter(first_name=request.GET.get('fname'))
    if request.GET.get('lname'):
        qs = qs.filter(last_name=request.GET.get('lname'))
    if request.GET.get('mail'):
        qs = qs.filter(last_name=request.GET.get('mail'))

    result = '<br>'.join(str(student) for student in qs)
    return render(request, 'student/students_list_one.html', {'students_list': result})


def students_list_two(request):
    qs = Student.objects.all()

    first_name, last_name, email = request.GET.get("fname"), request.GET.get("lname"), request.GET.get("mail")

    qs = qs.filter(Q(first_name=first_name) |
                   Q(last_name=last_name) |
                   Q(email=email))

    print(qs.query.sql_with_params())
    result = '<br>'.join(str(student) for student in qs)
    return render(request, 'student/students_list_two.html', {'students_list': result})
