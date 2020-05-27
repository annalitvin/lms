from django.db.models import Q


class StudentValidFormMixin:

    def form_valid(self, form):
        phone_number = form.cleaned_data.get('phone_number').strip()
        email = form.cleaned_data.get('email').strip()

        is_student_exists = self.model.objects.filter(Q(phone_number=phone_number) |
                                                      Q(email=email)).exists()
        if is_student_exists:
            error_massage = "Student not added. Student with such phone_number and email is exists! Try again:"
            return self.render_to_response(self.get_context_data(form=form, error_massage=error_massage, status=400))

        response = super().form_valid(form)
        return response
