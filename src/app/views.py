from django.http import HttpResponse


def main(request):
    return HttpResponse("Generate teachers in database using url: <strong> <a href='/teacher'>/teacher</a> </strong> "
                        "<br>" +
                        "or generate students in database using url: <strong> <a href='/student'>/student</a> </strong>"
                        + "<br><br>", status=200)
