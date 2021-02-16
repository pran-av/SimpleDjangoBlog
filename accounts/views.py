from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse # can change link name in future
from django.views.generic import CreateView
from django.http import HttpResponse


# Create your views here.
class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'user_registration.html'

    def get_success_url(self):
        return reverse('home')  # sends user to the success page

def login(request):
    return HttpResponse('login')
