from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy # can change link name in future
from django.views import generic


# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
