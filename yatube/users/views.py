from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import CreationForm

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        user = form.save()
        subject = 'Регистрация на сайте'
        message = 'Успешная регистрация на сайте.'
        from_email = 'maksimaster72@gmail.com'
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)

        return super().form_valid(form)
