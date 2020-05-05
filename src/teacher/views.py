from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
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
