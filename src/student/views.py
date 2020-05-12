from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse

from student.forms import StudentAddForm, StudentEditForm
from .models import Student


def index(request):
    return HttpResponse("Generate students in database using url: <strong> generate?student_number=1 </strong> <br>"
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
        return redirect('student:data_success')
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
        qs = qs.filter(email=request.GET.get('mail'))

    return render(request, 'student/students_list_one.html',
                  {'students_list': qs, 'title': 'Student list 1'})


def students_list_two(request):
    qs = Student.objects.all()

    first_name, last_name, email = request.GET.get("fname"), request.GET.get("lname"), request.GET.get("mail")

    if first_name or last_name or email:
        qs = qs.filter(Q(first_name=first_name) |
                       Q(last_name=last_name) |
                       Q(email=email))

    result = '<br>'.join(str(student) for student in qs)
    return render(request, 'student/students_list_two.html',
                  {'students_list': result, 'title': 'Student list 2'})


def students_add(request):

    students_add_template = 'student/students_add.html'

    if request.method == 'POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number').strip()
            email = form.cleaned_data.get('email').strip()

            is_student_exists = Student.objects.filter(Q(phone_number=phone_number) |
                                                       Q(email=email)).exists()
            if is_student_exists:
                error_massage = "Student not added. Student with such phone_number and email is exists! Try again:"
                return render(request, students_add_template, {'form': form, "error_massage": error_massage},
                              status=400)
            form.save()
            return HttpResponseRedirect(reverse('student:list_one'))
    else:
        form = StudentAddForm()

    return render(request, students_add_template,
                  {'form': form, 'title': 'Add student'})


def student_edit(request, id):

    students_edit_template = 'student/students_edit.html'
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponseNotFound(f"Student with id={id} doesn't exist")

    if request.method == 'POST':
        form = StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student:list_one'))
    else:
        form = StudentEditForm(instance=student)

    return render(request, students_edit_template,
                  {'form': form, 'title': 'Edit student'})


def student_delete(request, id):

    student = get_object_or_404(Student, id=id)
    student.delete()
    return HttpResponseRedirect(reverse('student:list_one'))
