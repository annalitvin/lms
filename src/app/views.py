from django.http import HttpResponse


def main(request):
    return HttpResponse("Generate teachers in database using url: <strong> gen_teacher?teach_number=1 </strong> <br>" +
                        "where teach_number is number of teachers. <br>Default: 100 teachers. <br><br>" +
                        "Or Generate students in database using url", status=200)